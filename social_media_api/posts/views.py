from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Post, Comment, Like  # Ensure Like is imported
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from notifications.models import Notification
from rest_framework.permissions import IsAuthenticated
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404  # Correct import
from django.views import generic


# Post View CRUD Operations
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Comment View CRUD Operations
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Feed View
class FeedView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        # Fetch all the users the current user is following
        following_users = user.following.all()
        # Return posts authored by followed users, ordered by creation date (newest first)
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

# Like Functionality
class PostLikeViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def like(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)  # Use get_object_or_404 correctly
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Create a notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target_content_type=ContentType.objects.get_for_model(Post),
                target_object_id=post.id
            )
            return Response({"message": "Post liked!"}, status=status.HTTP_201_CREATED)
        return Response({"message": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    def unlike(self, request, pk):
        post = get_object_or_404(Post, pk=pk)  # Use get_object_or_404 correctly
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"message": "Post unliked!"}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({"message": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

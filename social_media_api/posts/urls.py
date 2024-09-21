# social_media_api/posts/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, PostLikeViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include routes for posts and comments
    path('feed/', FeedView.as_view(), name='feed'),
    path('posts/<int:pk>/like/', PostLikeViewSet.as_view({'post': 'like'}), name='like-post'),  # Updated to include 'posts/' prefix
    path('posts/<int:pk>/unlike/', PostLikeViewSet.as_view({'delete': 'unlike'}), name='unlike-post'),  # Use 'delete' for unliking
]

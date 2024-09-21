# social_media_api/posts/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (PostViewSet, CommentViewSet, FeedView)
from .views import PostLikeViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
    path('<int:pk>/like/', PostLikeViewSet.as_view({'post': 'like'}), name='like-post'),
    path('<int:pk>/unlike/', PostLikeViewSet.as_view({'post': 'unlike'}), name='unlike-post'),
]
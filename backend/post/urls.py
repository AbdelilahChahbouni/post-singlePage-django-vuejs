from django.urls import path
from .api import PostListAPI , CommentListAPI , CommentCreateAPI , LikeCreateAPI , LikeListAPI  , LikeDestroyAPI

urlpatterns = [
path('api/list' , PostListAPI.as_view()),
path('api/comment/list/<int:pk>',CommentListAPI.as_view()),
path('api/comment/create',CommentCreateAPI.as_view()),
path('api/like/add', LikeCreateAPI.as_view()),
path('api/like/list/<int:pk>' , LikeListAPI.as_view()),
path('api/like/delete/<int:post_id>' , LikeDestroyAPI.as_view())


]
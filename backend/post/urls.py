from django.urls import path
from .api import PostListAPI , CommentListAPI , CommentCreateAPI , LikeCreateAPI

urlpatterns = [
path('api/list' , PostListAPI.as_view()),
path('api/comment/list',CommentListAPI.as_view()),
path('api/comment/create',CommentCreateAPI.as_view()),
path('api/like/add', LikeCreateAPI.as_view())

]
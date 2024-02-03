from .models import Post , Comment , Like
from .serializer import CommentListSerializer , PostListSerializer , LikeListSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view



class PostListAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class CommentListAPI(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

class CommentCreateAPI(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer


class LikeCreateAPI(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeListSerializer


from .models import Comment , Post , Like
from rest_framework import serializers


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fileds = '__all__'


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
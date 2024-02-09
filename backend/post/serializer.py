from .models import Comment , Post , Like
from rest_framework import serializers


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = '__all__'


class LikeListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Like
        fields = '__all__'
from .models import Post , Comment , Like
from .serializer import CommentListSerializer , PostListSerializer , LikeListSerializer
from rest_framework import generics , permissions , filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# from rest_framework.decorators import api_view, permission_classes
from rest_framework import status , serializers
from django.shortcuts import get_object_or_404



class PostListAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class CommentListAPI(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['create_at']
    def get_queryset(self):
        post_id = self.kwargs['pk']
        queryset = Comment.objects.filter(post_id=post_id)
        return queryset

class CommentCreateAPI(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    permission_classes = [IsAuthenticated] 
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)
            print(self.request.user)

   
      


class LikeListAPI(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeListSerializer
    def get_queryset(self):
        post_id = self.kwargs['pk']
        queryset = Like.objects.filter(post_id=post_id)
        return queryset
state = False
class LikeCreateAPI(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeListSerializer
    #permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        global state
        if self.request.user.is_authenticated:
            user = self.request.user
            post_id = self.request.data.get('post')  # Assuming 'post' is the field representing the post ID in the request data
            existing_like = Like.objects.filter(user=user, post_id=post_id).exists()
            state = existing_like
            print(user , post_id , existing_like ,state)
            if not existing_like:
                serializer.save(user=user)
                
    def create(self, request, *args, **kwargs):
        try:
            # Call the superclass's create method to perform object creation
            response = super().create(request, *args, **kwargs)
            # If the creation is successful, return a custom response
            return Response({'liked00': state}, status=status.HTTP_201_CREATED)
        except serializers.ValidationError:
            # Catch the validation error raised when the user has already liked the post
            return Response({'liked': True}, status=status.HTTP_400_BAD_REQUEST)
    

class LikeDestroyAPI(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeListSerializer
    permissions_classes = [IsAuthenticated]

    # def get_object(self):
    #     user = self.request.user
    #     post_id = self.kwargs.get('post_id')  # Assuming post_id is passed in the URL
    #     try:
    #         # Get the like instance associated with the current user and post
    #         return Like.objects.get(user=user, post_id=post_id)
    #     except Like.DoesNotExist:
    #         # If the like does not exist, return a 404 response
    #         return Response({'detail': 'Like does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    # def perform_create(self, serializer):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         # Only save the like if the user is authenticated
    #         serializer.save(user=user)
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     print(instance)
    #     self.perform_destroy(instance)
    #     return Response({'detail': 'Like removed successfully'}, status=status.HTTP_204_NO_CONTENT)

    # def perform_destroy(self, instance):
    #     instance.delete() 
        
    def get_object(self):
        user = self.request.user
        post_id = self.kwargs.get('post_id')  # Assuming post_id is passed in the URL
        return get_object_or_404(Like, user=user, post_id=post_id)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is not None:
            instance.delete()
            return Response({'message': 'true'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Like does not exist'}, status=status.HTTP_200_OK)

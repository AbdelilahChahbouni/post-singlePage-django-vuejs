from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializers import SignupSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.



# @api_view(['POST'])
# def resgister(request):
#     data = request.data
#     user = SignupSerializer(data=data)
#     if user.is_valid():
#         if not User.objects.filter(username=data['email']).exists():
#             user = User.objects.create(
#                 username = data['username'],

#                 email = data['email'],
#                 password = make_password(data['password']) 
#             )
#             return Response({'details': 'your account registerd successfully'},
#                             status=status.HTTP_201_CREATED)
#         else:
#             return Response({'details': 'this email already exists'},
#                             status=status.HTTP_400_BAD_REQUEST)

#     else:
#         return Response(user.errors)

class RegisterAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer


class CurrentUserAPI(generics.ListAPIView):
    serializer_class = SignupSerializer  # Use the serializer class directly
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get_queryset(self):
        # Filter the queryset to only return the current user
        return User.objects.filter(pk=self.request.user.pk)

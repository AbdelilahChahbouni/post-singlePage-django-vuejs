from django.urls import path
from .views import RegisterAPI ,CurrentUserAPI


urlpatterns = [
    path('register' , RegisterAPI.as_view() , name='register'),
    path('current_user' ,CurrentUserAPI.as_view() , name="current_user")
]
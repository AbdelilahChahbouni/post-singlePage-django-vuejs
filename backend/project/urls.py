
from django.contrib import admin
from rest_framework.authtoken import views as authtoken_views
from django.urls import path , include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/' ,include("post.urls") ),
    path('account/' ,include("acount.urls")),
    # path('api-auth/', include('rest_framework.urls')),  # Optional: For login and logout views
    #path('api-token-auth/', authtoken_views.obtain_auth_token),  # Token authentication view
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

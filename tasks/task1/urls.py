from django.urls import path
from tasks.task1.api_endpoints.UserCreate import UserCreateView
from tasks.task1.api_endpoints.UserLogin import UserActivateView
from tasks.task1.api_endpoints.UserDelete import UserDestroyView
from rest_framework.authtoken import views
from django.urls import path
from tasks.task1.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('logac/', UserActivateView.as_view(), name='activate'),
    path('loginnn/', views.obtain_auth_token),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create', UserCreateView.as_view()),
    path('user/<pk>/delete', UserDestroyView.as_view())
]

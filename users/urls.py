from django.urls import path
from .views import ProfileUpdateView, ProfileView, SignUpView, logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('auth/user/login/', auth_views.LoginView.as_view(), name='login'),
    path('auth/user/logout/', logout_view, name='logout'),
    path('auth/user/signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile-edit'),
    # other paths
]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.user_signup, name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('password_change/', views.password_change, name="password_change"),
    path('password_change_wp/', views.password_change_wp, name="password_change_wp"),
]

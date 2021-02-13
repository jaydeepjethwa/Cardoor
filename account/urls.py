from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.profile_page, name='account'),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout")
]
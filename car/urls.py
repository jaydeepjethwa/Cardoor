from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.home, name="home"),
    path('carlist/', views.carlist, name="carlist"),
    path('cardetail/<int:id>', views.cardetail),
    path('carrent/', views.carrent, name="carrent"),
    path('booking/', views.booking, name='booking'),

]
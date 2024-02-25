from django.urls import path
from base import views as base_views

urlpatterns = [
    path("" ,  base_views.homePage , name = "home-page") ,
]
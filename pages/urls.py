from django.urls import path
from .views import *  # importa de .views todas las funciones

urlpatterns = [
    path("", homePageview, name="home"),
]

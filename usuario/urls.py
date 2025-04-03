from django.urls import path
from . import views
# Create your views here.

urlpatterns = [
    path("login/", views.login, name="login"),
    path("register/" , views.register , name="register"),
    path("home" , views.home , name="home"),
    path("receber_coordenadas" , views.receber_coordenadas, name="receber_coordenadas")
]
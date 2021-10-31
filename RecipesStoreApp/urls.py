from django.urls import path
from . import views


#path --> direccion de la url
urlpatterns = [
    path('', views.index, name='index'),
]
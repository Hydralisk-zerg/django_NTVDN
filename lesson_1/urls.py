from operator import index
from django.urls import path
from lesson_1 import views 

urlpatterns = [
    path('', views.index, name="index"),
]

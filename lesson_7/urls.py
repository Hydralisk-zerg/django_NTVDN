from django.urls import path
from lesson_7 import views 

urlpatterns = [
    path('', views.index, name='index'),
]
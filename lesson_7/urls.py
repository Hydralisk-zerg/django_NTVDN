from django.urls import path
from lesson_7 import views 

urlpatterns = [
    path('try-form/', views.my_form, name='my_form'),
]
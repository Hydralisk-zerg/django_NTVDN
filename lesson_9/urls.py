from argparse import Namespace
from django.urls import path, include
from lesson_9 import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'game', views.GameVievsSet)
router.register(r'gamer', views.GamerVievsSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

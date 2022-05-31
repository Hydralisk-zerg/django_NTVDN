from django.shortcuts import render

from lesson_8.models import GameModel, GamerModel
from rest_framework import viewsets
from lesson_9.serializers import GameModelSerializer, GamerModelSerializer


class GameVievsSet(viewsets.ModelViewSet):
    queryset = GameModel.objects.all().order_by('-year')
    serializer_class = GameModelSerializer


class GamerVievsSet(viewsets.ModelViewSet):
    queryset = GamerModel.objects.all()
    serializer_class = GamerModelSerializer
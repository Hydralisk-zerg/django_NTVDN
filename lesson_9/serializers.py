from django_restart.settings import REST_FRAMEWORK


from rest_framework import serializers
from lesson_8.models import GameModel, GamerModel


class GameModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameModel
        fields = '__all__'


class GamerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamerModel
        fields = ['nickname', 'email']
        
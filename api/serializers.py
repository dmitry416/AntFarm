from rest_framework import serializers
from game.models import *


class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'ant_count']


class UserAntsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnts
        fields = ['ant_id', 'count']

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

class BossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boss
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'cost']

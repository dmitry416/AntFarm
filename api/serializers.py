from rest_framework import serializers
from game.models import *


class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'ant_count']


class UserAntsSerializer(serializers.ModelSerializer):
    ant_image = serializers.SlugRelatedField(source='ant', slug_field='path_to_image', read_only=True)
    ant_name = serializers.SlugRelatedField(source='ant', slug_field='name', read_only=True)
    cost = serializers.SerializerMethodField()

    class Meta:
        model = UserAnts
        fields = ['ant_image', 'count', 'cost', 'ant_name', 'is_sent']

    def get_cost(self, obj):
        return obj.get_cost()

class BossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boss
        fields = '__all__'

class UserItemsSerializer(serializers.ModelSerializer):
    item_image = serializers.SlugRelatedField(source='item', slug_field='path_to_image', read_only=True)
    item_name = serializers.SlugRelatedField(source='item', slug_field='name', read_only=True)
    item_cost = serializers.SlugRelatedField(source='item', slug_field='cost', read_only=True)

    class Meta:
        model = UserItems
        fields = ['item_image', 'item_name', 'count', 'item_cost']


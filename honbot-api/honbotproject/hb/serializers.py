from rest_framework import serializers
from .models import Player, Match, Item


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        depth = 1
        exclude = ('rnk_history', 'cs_history', 'acc_history', 'history_updated')


class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        depth = 1


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'name', 'cli_name', 'cost', 'description')

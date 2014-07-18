from rest_framework import serializers
from .models import Player, Match


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        depth = 1


class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        depth = 1

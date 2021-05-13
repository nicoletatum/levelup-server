"""View module for handling requests about park areas"""
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from levelupapi.models import Event, Player, Game


class Profile(ViewSet):
    """Player can see profile information"""

    def list(self, request):
        """Handle GET requests to profile resource

        Returns:
            Response -- JSON representation of user info and events
        """
        player = Player.objects.get(user=request.auth.user)
        events = Event.objects.filter(attendee=player)

        events = EventSerializer(
            events, many=True, context={'request': request})
        player = PlayerSerializer(
            player, many=False, context={'request': request})

        # Manually construct the JSON structure you want in the response
        profile = {}
        profile["player"] = player.data
        profile["events"] = events.data

        return Response(profile)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for player's related Django user"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')


class PlayerSerializer(serializers.ModelSerializer):
    """JSON serializer for players"""
    user = UserSerializer(many=False)

    class Meta:
        model = Player
        fields = ('user', 'bio')


class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games"""
    class Meta:
        model = Game
        fields = ('name',)


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events"""
    game = GameSerializer(many=False)

    class Meta:
        model = Event
        fields = ('id', 'game', 'description', 'date', 'time')

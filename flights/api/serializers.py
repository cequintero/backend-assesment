from rest_framework import serializers
from api.models import Itinerary, Agent

class AgentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields = ['name','rating']

class ItinerarySerializers(serializers.ModelSerializer):

    agent = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    agent_rating = serializers.SlugRelatedField(
        source='agent',
        many=False,
        read_only=True,
        slug_field='rating'
    )

    class Meta:
        model = Itinerary
        fields = ['id','legs', 'price','agent', 'agent_rating']

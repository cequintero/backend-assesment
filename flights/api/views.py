from rest_framework.response import Response
from .models import Itinerary
from rest_framework.views import APIView
from .serializers import ItinerarySerializers


class Itinerary_APIView(APIView):

    def get(self, request):
        agent = request.GET.get('agent', None)
        itineraries = Itinerary.objects.all()
        if agent:
            itineraries = itineraries.filter(agent__name__contains=agent)
        serializer = ItinerarySerializers(itineraries, many=True)
        return Response(serializer.data)

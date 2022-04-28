from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('v1/flights/', Itinerary_APIView.as_view()),
]
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Agent(models.Model):
    name = models.CharField(max_length=255)
    rating = models.FloatField()

    def __str__(self):
        return self.name


class Leg(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    departure_airport = models.CharField(max_length=255)
    arrival_airport = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    stops = models.IntegerField()
    airline_name = models.CharField(max_length=255)
    airline_id = models.CharField(max_length=255)
    duration_mins = models.IntegerField()

    def __str__(self):
        return self.id


class Itinerary(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    price = models.CharField(max_length=20,validators=[RegexValidator(
        regex='^.\d+(\.\d{1,2})?$', message='invalid price')])
    agent = models.ForeignKey(Agent, on_delete=models.RESTRICT)
    legs = models.ManyToManyField(Leg)

    def __str__(self):
        return self.id

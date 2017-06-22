import graphene
from graphene_django.types import DjangoObjectType
from cars.models import Color, Car

class CarType(DjangoObjectType):
    class Meta:
        model = Car

class ColorType(DjangoObjectType):
    class Meta:
        model = Color

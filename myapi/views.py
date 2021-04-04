# views.py
from rest_framework import viewsets

from .serializers import HeroSerializer#, FlowerSerializer
from .models import Hero, Flowering


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


#class FlowerViewSet(viewsets.ModelViewSet):
#    queryset = Flowering.objects.all().order_by('name')
 #   serializer_class = FlowerSerializer

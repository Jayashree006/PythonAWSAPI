# serializers.py
from rest_framework import serializers

from .models import Hero, Flowering


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')


#class FlowerSerializer(serializers.HyperlinkedModelSerializer):
 #   class Meta:
  #      model = Flowering
   #     fields = ('name', 'colour')

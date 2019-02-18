from rest_framework import serializers
 
from . import models
 
class WineCollectionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = models.WineCollection
        fields = '__all__'
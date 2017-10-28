from rest_framework import serializers
from .models import meditations

class MeditationsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = meditations
        field = '__all__'

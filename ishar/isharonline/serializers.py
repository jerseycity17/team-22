from rest_framework import serializers
from .models import meditations

class MeditationsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = meditations
        fields = '__all__'

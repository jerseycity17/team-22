from isharonline import meditation
from rest_framework import serializers


class meditationsSerializer (serializers.Serializer):
    title = serializers.CharField(read_only=True)

def create(self, validated_data):
    return meditation.objects.create(**validated_data)

def update(self, instance, validated_data):
    instance.title = validated_data.get('title, instance.title')
    return instance



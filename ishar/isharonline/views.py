import sys
sys.path.append("..")

import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ishar.settings")
django.setup()

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import meditations
from .serializers import MeditationsSerializer

def index(request):
    return render(request, "isharonline/index.html")

def library(request):
    return render(request, "isharonline/library.html")

class MeditationList(APIView):

    def get(self, request):
        m = meditations.objects.all()
        serializers = MeditationsSerializer(m, many=True)
        return Response(serializers.data)

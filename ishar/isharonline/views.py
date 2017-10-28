from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "isharonline/index.html")


def library(request):
    return render(request, "isharonline/library.html")

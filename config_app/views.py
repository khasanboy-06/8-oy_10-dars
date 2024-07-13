from django.shortcuts import render

from rest_framework import generics
from rest_framework import authentication

from .models import Video
from .serializers import VideoSerializer

class VideoView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


    
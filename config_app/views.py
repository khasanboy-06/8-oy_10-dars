from django.shortcuts import render

from rest_framework import generics

from .models import Video
from .serializers import VideoSerializer
from .permissions import VideoPermission

class VideoCreateView(generics.ListCreateAPIView, generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [VideoPermission]


class VideoUpdateView(generics.RetrieveUpdateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [VideoPermission]
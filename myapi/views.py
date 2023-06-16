from django.shortcuts import render,redirect
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .serializers import HeroSerializer
from .models import Hero
from rest_framework.generics import ListAPIView

# Create your views here.

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
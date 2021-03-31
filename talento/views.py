from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
from rest_framework import viewsets, permissions

from talento import models
from talento.serializers import EntradaSerializer
from rest_framework.authtoken.models import Token


class EntradaViewSet(viewsets.ModelViewSet):
    queryset = models.Entrada.objects.all()
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = EntradaSerializer



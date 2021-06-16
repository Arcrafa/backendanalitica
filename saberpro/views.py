# Create your views here.
from rest_framework import viewsets, permissions

from saberpro import models
from saberpro.serializers import SaberProSerializer
from rest_framework.authtoken.models import Token


class SaberProViewSet(viewsets.ModelViewSet):
    queryset = models.Saberpro.objects.all()
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = SaberProSerializer
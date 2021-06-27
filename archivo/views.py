


# Create your views here.
from rest_framework import viewsets, permissions

from archivo import models
from archivo.serializers import ArchivoSerializer
from rest_framework.authtoken.models import Token


class ArchivoViewSet(viewsets.ModelViewSet):
    queryset = models.Archivo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArchivoSerializer

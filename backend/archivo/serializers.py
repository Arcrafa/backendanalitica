from rest_framework import serializers

from backend.archivo import models


class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Archivo
        fields = '__all__'




from rest_framework import serializers

from archivo import models


class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Archivo
        fields = '__all__'




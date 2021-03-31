from rest_framework import serializers

from talento import models


class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Entrada
        fields = '__all__'




from rest_framework import serializers

from saberpro import models


class SaberProSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Saberpro
        fields = '__all__'

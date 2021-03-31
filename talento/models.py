from django.db import models

# Create your models here.
# Create your models here.
from django.db import models
from analitica import settings
from django.contrib.auth.models import User


class Entrada(models.Model):
    nombre = models.CharField(max_length=100)
    archivo = models.FileField(upload_to="archivos/", null=True, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    #created = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='created_by', blank=True, null=True)


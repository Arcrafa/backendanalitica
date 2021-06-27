from django.db import models


class Archivo(models.Model):
    # id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    new_file = models.FileField(upload_to="archivos/", null=True, blank=True)
    fecha_creacion = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=15, blank=True, null=True)
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'archivo'

from django.db import models

class alumno(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
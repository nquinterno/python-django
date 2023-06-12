from django.db import models
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.EmailField() #numero_curso = models.IntegerField(6)
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.EmailField(null=True, default=None)
    
class Curso(models.Model):
    numero_curso = models.IntegerField(6)
    tipo_curso = models.CharField(max_length=20)
    
class Entregable(models.Model):
    numero_curso = models.IntegerField(6)
    tarea = models.CharField(max_length=40)
    vencimiento = models.DateTimeField()
    
class Usuario(models.Model) :
        usuario = models.CharField(max_length=10)
        password = models.CharField(max_length=10)
        mail = models.EmailField()
        nombre = models.CharField(max_length=40)
        apellido = models.CharField(max_length=40)


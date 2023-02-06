from django.db import models

# Create your models here.
class Profesional (models.Model):
    nombre_completo = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    dni = models.CharField(max_length=9)
    especialidad = models.CharField(max_length=40)
    esta_recibido = models.BooleanField()
    esta_activo = models.BooleanField()

class Paciente (models.Model):
    especie = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    peso = models.IntegerField()
    nombre = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=20)
    esta_castrado = models.BooleanField(blank=True)
    direccion = models.CharField(max_length=50)
    dni_tutor = models.CharField(max_length=9)
    descripcion = models.CharField(max_length=500, blank=True)

class Visita (models.Model):
    fecha_visita = models.DateField()
    nombre_paciente = models.CharField(max_length=20)
    nombre_profesional = models.CharField(max_length=50)
    diagnostico = models.CharField(max_length=1000)
    medicacion = models.CharField(max_length=500, blank=True)
    proximo_control = models.DateField(blank=True, null=True)
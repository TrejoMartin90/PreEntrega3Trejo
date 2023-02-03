from django.db import models

# Create your models here.
class Profesional (models.Model):
    nombre_completo = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    dni = models.CharField(max_length=9)
    especialidad = models.CharField(max_length=40)
    esta_recibido = models.BooleanField()
    activo = models.BooleanField()

class Paciente (models.Model):
    especie = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=20)
    castrado = models.BooleanField()
    direccion = models.CharField(max_length=50)
    dni_tutor = models.CharField(max_length=9)

class Visita (models.Model):
    fecha_visita = models.DateField()
    nombre_paciente = models.CharField(max_length=20)
    nombre_profesional = models.CharField(max_length=50)
    diagnostico = models.CharField(max_length=300)
    medicacion = models.CharField(max_length=200, blank=True)
    proximo_control = models.DateField(blank=True)





    
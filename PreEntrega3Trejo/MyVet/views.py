from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request,"MyVet/home.html")

def ver_profesionales (request):
	return render(request,"MyVet/ver_profesionales.html")

def ver_visitas (request):
	return render(request,"MyVet/ver_visitas.html")

def ver_pacientes (request):
	return render(request,"MyVet/ver_pacientes.html")

def crear_profesional (request):
	return render(request,"MyVet/crear_profesional.html")

def crear_visita (request):
	return render(request,"MyVet/crear_visita.html")

def crear_paciente (request):
	return render(request,"MyVet/crear_paciente.html")
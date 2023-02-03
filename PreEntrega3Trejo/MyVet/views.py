from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return HttpResponse('Home Page')

def ver_profesionales (request):
	return HttpResponse("Listado de Profesionales")

def ver_visitas (request):
	return HttpResponse("Listado de Visitas")

def ver_pacientes (request):
	return HttpResponse("Listado de Pacientes")

def crear_profesional (request):
	return HttpResponse("Creación de Profesional")

def crear_visita (request):
	return HttpResponse("Creación de Visitas")

def crear_paciente (request):
	return HttpResponse("Creación de Pacientes")
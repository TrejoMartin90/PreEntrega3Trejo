from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def home(request):
	return render(request,"MyVet/home.html")

def ver_profesionales (request):
	return render(request,"MyVet/ver_profesionales.html")

def ver_visitas (request):
	return render(request,"MyVet/ver_visitas.html")
	

def ver_pacientes (request):
	pacientes = Paciente.objects.all().order_by("nombre").values()
	return render(request,"MyVet/ver_pacientes.html",{"pacientes": pacientes})

def crear_profesional (request):
	if request.method == "POST":
		miFormulario = ProfesionalFormulario(request.POST)
		print(miFormulario)
		if miFormulario.is_valid():
			informacion = miFormulario.cleaned_data
			nuevoProfesional = Profesional(nombre_completo=informacion["nombre_completo"],fecha_nacimiento = informacion["fecha_nacimiento"],email=informacion["email"],dni=informacion["dni"],especialidad=informacion["especialidad"],esta_recibido=informacion["esta_recibido"],esta_activo=True)
			nuevoProfesional.save()
			return render(request, "MyVet/home.html")
	else:
			miFormulario = ProfesionalFormulario()
	return render(request, "MyVet/crear_profesional.html", {"miFormulario": miFormulario})  

def crear_visita (request):
	if request.method == "POST":
		miFormulario = VisitaFormulario(request.POST)
		print(miFormulario)
		if miFormulario.is_valid():
			informacion = miFormulario.cleaned_data
			nuevaVisita = Visita(fecha_visita = informacion["fecha_visita"],nombre_paciente=informacion["nombre_paciente"],nombre_profesional=informacion["nombre_profesional"],diagnostico=informacion["diagnostico"],medicacion=informacion["medicacion"],proximo_control=informacion["proximo_control"])
			nuevaVisita.save()
			return render(request, "MyVet/home.html")
	else:
			miFormulario = VisitaFormulario()
	return render(request, "MyVet/crear_visita.html", {"miFormulario": miFormulario})


def crear_paciente (request):
	if request.method == "POST":
		nuevoPaciente = Paciente(nombre=request.POST["nombre"],especie=request.POST["especie"],raza=request.POST["raza"],fecha_nacimiento=request.POST["fecha_nacimiento"],peso=request.POST["peso"],sexo=request.POST["sexo"],esta_castrado=request.POST["esta_castrado"],dni_tutor=request.POST["dni_tutor"],descripcion=request.POST["descripcion"])
		nuevoPaciente.save()
		return render(request, "MyVet/home.html")
	return render(request,"MyVet/crear_paciente.html")

def buscar_paciente(request):
	return render(request, "MyVet/buscar_paciente.html")

def buscar_paciente_result(request):
	if request.GET["nombre"]:
		nombre = request.GET["nombre"]
		pacientes = Paciente.objects.filter(nombre__icontains=nombre)
		return render(request,"MyVet/buscar_paciente_result.html", {"pacientes": pacientes, "nombre":nombre})
	else:
		respuesta = "No se han enviado datos"
	return HttpResponse(respuesta)

def buscar_pacientes(request):
	pacientes = Paciente.objects.filter()
	return render(request,"MyVet/buscar_paciente_result.html", {"pacientes": pacientes})
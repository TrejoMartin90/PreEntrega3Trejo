from django.urls import path
from MyVet import views

urlpatterns = [
    path('', views.home, name = "Home"),
    path('profesionales', views.ver_profesionales, name="Ver Profesionales"),
    path('pacientes', views.ver_pacientes, name="Ver Pacientes"),
    path('visitas', views.ver_visitas, name="Ver Visitas"),
    path('crearProfesional', views.crear_profesional, name="Crear Profesionales"),
    path('crearPaciente', views.crear_paciente, name="Crear Paciente"),
    path('crearVisita', views.crear_visita, name="Crear Visita"),
]
from django import forms

#Se crean estas variables para definir los valores de los campos de tipo dropdown
opciones_sexo = [
    ("Macho","Macho"),
    ("Hembra","Hembra")
]

opciones_boolean = [
    ("True","Si"),
    ("False","No")
]

class ProfesionalFormulario (forms.Form):
    nombre_completo = forms.CharField()
    fecha_nacimiento = forms.DateField(widget=forms.NumberInput(attrs={"type":"date"}))
    email = forms.EmailField()
    dni = forms.CharField()
    especialidad = forms.CharField()
    esta_recibido = forms.CharField(label="Está Recibido?", widget=forms.Select(choices=opciones_boolean))

class PacienteFormulario (forms.Form):
    especie = forms.CharField()
    raza = forms.CharField()
    peso = forms.IntegerField()
    nombre = forms.CharField()
    fecha_nacimiento = forms.DateField()
    sexo = forms.CharField(label="Sexo", widget=forms.Select(choices=opciones_sexo))
    esta_castrado = forms.BooleanField()
    direccion = forms.CharField()
    dni_tutor = forms.CharField()
    descripcion = forms.CharField()

class VisitaFormulario (forms.Form):
    fecha_visita = forms.DateField(widget=forms.NumberInput(attrs={"type":"date"}))
    nombre_paciente = forms.CharField()
    nombre_profesional = forms.CharField()
    diagnostico = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    medicacion = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), required=False)
    proximo_control = forms.DateField(widget=forms.NumberInput(attrs={"type":"date"}),required=False)
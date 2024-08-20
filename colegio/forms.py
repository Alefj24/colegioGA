from django import forms
from django.contrib.auth.models import User
from .models import Estudiante, Profesor, Rector, Curso, Salon, Asignacion, Asistencia, Nota

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['usuario', 'nombre', 'apellido']


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['usuario', 'materia', 'nombre', 'apellido']


class RectorForm(forms.ModelForm):
    class Meta:
        model = Rector
        fields = ['usuario', 'nombre', 'apellido']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion']

class SalonForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = ['numero_salon']

class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = ['curso', 'profesor', 'salon']

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['asignacion', 'estudiante', 'fecha', 'estado']

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['asignacion', 'estudiante', 'nota', 'fecha']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


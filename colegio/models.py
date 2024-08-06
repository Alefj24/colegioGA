from django.db import models
from django.contrib.auth.models import User

# En el archivo `models.py`
# En el archivo `models.py`
class Estudiante(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    nombre = models.CharField(max_length=100, default='Nombre')  # Añadir un valor predeterminado
    apellido = models.CharField(max_length=100, default='Apellido')  # Añadir un valor predeterminado
    def __str__(self):
        return f'{self.usuario.get_full_name()} - {self.nombre} - {self.apellido}'
# En el archivo `models.py`
class Profesor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    materia = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100, default='Nombre')  # Añadir un valor predeterminado
    apellido = models.CharField(max_length=100, default='Apellido')  # Añadir un valor predeterminado
    def __str__(self):
        return f'{self.usuario.get_full_name()} - {self.materia} - {self.nombre} - {self.apellido}'

# En el archivo `models.py`
class Rector(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    nombre = models.CharField(max_length=100, default='Nombre')  # Añadir un valor predeterminado
    apellido = models.CharField(max_length=100, default='Apellido')  # Añadir un valor predeterminado
    def __str__(self):
        return f'{self.usuario.get_full_name()} - {self.nombre} - {self.apellido}'
# Modelo Curso
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# Modelo Salon
class Salon(models.Model):
    numero_salon = models.IntegerField(primary_key=True)

    def __str__(self):
        return f'Salon {self.numero_salon}'

# Modelo Asignacion
class Asignacion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.curso.nombre} - {self.profesor.usuario.get_full_name()}'

# Modelo Asistencia
class Asistencia(models.Model):
    ASISTENCIA_ESTADO_CHOICES = [
        ('presente', 'Presente'),
        ('falla', 'Falla')
    ]
    asignacion = models.ForeignKey(Asignacion, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.CharField(max_length=8, choices=ASISTENCIA_ESTADO_CHOICES)

    def __str__(self):
        return f'{self.estudiante.usuario.get_full_name()} - {self.fecha} - {self.estado}'

# Modelo Nota
class Nota(models.Model):
    asignacion = models.ForeignKey(Asignacion, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f'{self.estudiante.usuario.get_full_name()} - {self.nota}'

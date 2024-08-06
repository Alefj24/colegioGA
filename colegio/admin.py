from django.contrib import admin
from .models import Estudiante, Profesor, Rector, Curso, Salon, Asignacion, Asistencia, Nota

class EstudianteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Estudiante._meta.fields]

class ProfesorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profesor._meta.fields]

class RectorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Rector._meta.fields]

class CursoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Curso._meta.fields]

class SalonAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Salon._meta.fields]

class AsignacionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Asignacion._meta.fields]

class AsistenciaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Asistencia._meta.fields]

class NotaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Nota._meta.fields]

admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Rector, RectorAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Salon, SalonAdmin)
admin.site.register(Asignacion, AsignacionAdmin)
admin.site.register(Asistencia, AsistenciaAdmin)
admin.site.register(Nota, NotaAdmin)
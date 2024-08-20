"""
URL configuration for colegioGA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from colegio import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/registrar/', views.registrar_estudiante, name='registrar_estudiante'),
    path('estudiantes/<int:pk>/actualizar/', views.actualizar_estudiante, name='actualizar_estudiante'),
    path('estudiantes/<int:pk>/eliminar/', views.eliminar_estudiante, name='eliminar_estudiante'),

    path('notas/', views.lista_notas, name='lista_notas'),
    path('notas/registrar/', views.registrar_nota, name='registrar_nota'),
    path('notas/<int:pk>/actualizar/', views.actualizar_nota, name='actualizar_nota'),
    path('mi_grupo/', views.mi_grupo, name='mi_grupo'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from .models import Estudiante, Nota
from .forms import EstudianteForm, NotaForm

@login_required
@permission_required('colegio.add_estudiante', raise_exception=True)
def registrar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'estudiantes/registrar_estudiante.html', {'form': form})

@login_required
@permission_required('colegio.change_estudiante', raise_exception=True)
def actualizar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'estudiantes/actualizar_estudiante.html', {'form': form})

@login_required
@permission_required('colegio.delete_estudiante', raise_exception=True)
def eliminar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('lista_estudiantes')
    return render(request, 'estudiantes/eliminar_estudiante.html', {'estudiante': estudiante})

@login_required
@permission_required('colegio.view_estudiante', raise_exception=True)
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/lista_estudiantes.html', {'estudiantes': estudiantes})

@login_required
@permission_required('colegio.add_nota', raise_exception=True)
def registrar_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaForm()
    return render(request, 'notas/registrar_nota.html', {'form': form})

@login_required
@permission_required('colegio.change_nota', raise_exception=True)
def actualizar_nota(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaForm(instance=nota)
    return render(request, 'notas/actualizar_nota.html', {'form': form})

@login_required
@permission_required('colegio.view_nota', raise_exception=True)
def lista_notas(request):
    notas = Nota.objects.select_related('estudiante').all()
    return render(request, 'notas/lista_notas.html', {'notas': notas})


@login_required
def mi_grupo(request):
    user = request.user
    grupos = user.groups.all()
    return render(request, 'mi_grupo.html', {'grupos': grupos})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('lista_estudiantes')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('user_login')
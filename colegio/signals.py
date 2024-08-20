from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group, Permission
from .models import Estudiante, Profesor, Rector

@receiver(post_save, sender=Estudiante)
def add_user_to_estudiante_group(sender, instance, **kwargs):
    estudiante_group, created = Group.objects.get_or_create(name='Estudiante')
    instance.usuario.groups.add(estudiante_group)

@receiver(post_save, sender=Profesor)
def add_user_to_profesor_group(sender, instance, **kwargs):
    profesor_group, created = Group.objects.get_or_create(name='Profesor')
    instance.usuario.groups.add(profesor_group)

@receiver(post_save, sender=Rector)
def add_user_to_rector_group(sender, instance, **kwargs):
    rector_group, created = Group.objects.get_or_create(name='Rector')
    instance.usuario.groups.add(rector_group)

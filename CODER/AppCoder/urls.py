from re import template
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path ('', inicio, name = 'inicio'),
    path ('pagEstudiantes/', pagEstudiantes, name = 'pagEstudiantes'),
    path ('cursos/', cursoForm, name = 'cursos'),
    path ('profesores/', formProfe, name = 'profesores'),
    path ('estudiantes/', formestudiantes, name = 'estudiantes'),
    path ('busquedaCamada/', busquedaCamada, name = 'busquedaCamada'),
    path ('buscar/', buscar),
    path ('leerProfesores/', leerProfesores, name = 'leerProfesores'),
    path ('eliminarProfesor/<nombre_profesor>', eliminarProfesor, name = 'eliminarProfesor'),
    path ('editarProfesor/<nombre_profesor>', editarProfesor, name = 'editarProfesor'),
    path ('estudiante/list', EstudiantesList.as_view(), name = 'List'),
    path ('estudiante/<pk>', EstudianteDetalle.as_view(), name = 'Detail'),
    path ('estudiante/nuevo/', EstudianteCreacion.as_view(), name = 'New'),
    path ('estudiante/editar/<pk>', EstudianteUpdate.as_view(), name = 'Edit'),
    path ('estudiante/borrar/<pk>', EstudianteDelete.as_view(), name = 'Delete'),

    path ('login', login_request, name = 'login'),
    path ('register', register, name = 'register'),
    path ('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name = 'logout'),
    path ('editarPerfil', editarPerfil, name = 'editarPerfil'),

]
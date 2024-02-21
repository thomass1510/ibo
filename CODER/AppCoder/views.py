from ast import Not
from email.mime import image
import re
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from pkg_resources import require
from AppCoder.models import *
from AppCoder.forms import CursoForm,FormProf,Formestudiantes,UserRegisterForm,UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def curso(self):

    curso=Curso(nombre = 'Django', camada = '9393939')
    curso.save()
    doc = f"Curso {curso.nombre} camada {curso.camada}"

    return HttpResponse(doc)

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def terminarRegistro(request):
    return render(request, "AppCoder/terminarRegistro.html")

def formestudiantes(request):


    if request.method == "POST":

        form=Formestudiantes(request.POST)  
        print(form)
        if form.is_valid:

            info = form.cleaned_data
            nombre = info['nombre']
            apellido = info['apellido']
            email = info['email']
            estudiante = Estudiante (nombre=nombre, apellido=apellido,email=email)
            estudiante.save()
            return render(request, "AppCoder/inicio.html")

    else:
        form = Formestudiantes()
    return render(request, "AppCoder/estudiantes.html", {"formulario":form})
@login_required
def cursoForm(request):



    if request.method == "POST":

        form=CursoForm(request.POST)  
        print(form)
        if form.is_valid:

            info = form.cleaned_data
            nombre = info['nombre']
            camada = info['camada']
            curso = Curso (nombre=nombre, camada=camada)
            curso.save()
            return render(request, "AppCoder/inicio.html")

    else:
        form = CursoForm()
    return render(request, "AppCoder/cursos.html", {"formulario":form})
@login_required
def formProfe(request):


    if request.method == "POST":

        form=FormProf(request.POST)  
        print(form)
        if form.is_valid:

            info = form.cleaned_data
            nombre = info['nombre']
            apellido = info['apellido']
            email = info['email']
            profesion = info['profesion']
            profesor = Profesor (nombre=nombre, apellido=apellido,email=email,profesion=profesion)
            profesor.save()
            return render(request, "AppCoder/inicio.html")

    else:
        form = FormProf()
    return render(request, "AppCoder/profesores.html", {"formulario":form})


def busquedaCamada(request):


    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):

    if request.GET['camada']:

        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos":cursos, "camada": camada})
    else:   
        return render(request, "AppCoder/busquedaCamada.html", {"error": "NO se ingreso ninguna camada"})
    
@login_required
def leerProfesores(request):



    profesores= Profesor.objects.all()
    contexto = {"profesores":profesores}    
    return render(request, "AppCoder/leerProfesores.html",contexto)

def eliminarProfesor(request,nombre_profesor):

    profesor = Profesor.objects.get(nombre = nombre_profesor)
    profesor.delete()

    profesores = Profesor.objects.all()

    contexto = {"profesores":profesores}

    return render(request,"AppCoder/leerProfesores.html",contexto)


def editarProfesor(request,nombre_profesor):

    profesor = Profesor.objects.get(nombre = nombre_profesor)


    if request.method == "POST":

        miFormulario = FormProf(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():

                informacion = miFormulario.cleaned_data

                profesor.nombre = informacion["nombre"]
                profesor.apellido = informacion["apellido"]
                profesor.mail = informacion["email"]
                profesor.profesion = informacion["profesion"]

                profesor.save()

                return render(request, "AppCoder/inicio.html")
    
    else:

        miFormulario = FormProf(initial = {'nombre' : profesor.nombre, 'apellido' : profesor.apellido, 'email' : profesor.email, 'profesion' : profesor.profesion})


    return render(request, "AppCoder/editarProfesor.html", {"formulario":miFormulario, "nombre_profesor": nombre_profesor})

@login_required
def pagEstudiantes(request):



    return render(request, "AppCoder/pagEstudiantes.html")

class EstudiantesList(ListView):


    model = Estudiante
    template_name = "AppCoder/estudiante_list.html"


class EstudianteDetalle(DetailView):

    model = Estudiante
    template_name = "AppCoder/estudiante_detalle.html"


class EstudianteCreacion(CreateView):

    model = Estudiante
    success_url= reverse_lazy("List")
    fields = ['nombre', 'apellido']


class EstudianteUpdate(UpdateView):

    model = Estudiante
    success_url= reverse_lazy("List")
    fields = ['nombre', 'apellido', 'email']


class EstudianteDelete(DeleteView):

    model = Estudiante
    success_url= reverse_lazy("List")

def login_request(request):


    if request.method == 'POST':
            form = AuthenticationForm(request, data =request.POST)

            if form.is_valid():
                usuario= request.POST['username']
                clave= request.POST['password']

                user=authenticate(username=usuario, password=clave)


                if usuario is not None:
                    login(request,user)

                    return render(request,"AppCoder/inicio.html", {'form':form,"mensaje":f"Bienvenido {usuario}"})
                else:

                    return render(request,"AppCoder/login.html", {'form':form,"mensaje": "Error, datos incorrectos"})
            else:   

                return render(request,"AppCoder/login.html", {'form':form,"mensaje": "Error, formulario erroneo"})
    
    form = AuthenticationForm()

    return render(request,"AppCoder/login.html", {'form': form})


def register(request):

    
    if request.method == "POST":

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']

            form.save()
            return render(request,"AppCoder/inicio.html", {'form':form,"mensajeRegistro":f"Usuario creado: {username} "},)
        
    else:
        form = UserRegisterForm()

    return render(request,"AppCoder/register.html", {'form':form})

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        formulario = UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():

            informacion = formulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request, "AppCoder/inicio.html",{'usuario':usuario, 'mensaje':'Perfil editado con exito'})
    else:
        formulario= UserEditForm(instance=usuario)


    return render(request, "AppCoder/editarPerfil.html",{"formulario":formulario, "usuario":usuario})



from dataclasses import fields
from tkinter import image_names
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    camada= forms.IntegerField()

class FormProf(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email= forms.EmailField()
    profesion = forms.CharField(max_length=50)

class Formestudiantes(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email= forms.EmailField()


class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts={k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email= forms.EmailField(label="Modificar EMAIL")
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña',widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre',max_length=50)
    last_name = forms.CharField(label='Apellido',max_length=50)

    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']
        help_texts={k:"" for k in fields}


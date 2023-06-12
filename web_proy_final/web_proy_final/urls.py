"""web_proy_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from web_proy_final.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",inicio, name="Inicio"),
    path("Estudiantes/",Estudiantes, name="Estudiantes"),
    path("EstudiantesForm/",EstudiantesForm, name="EstudiantesForm"),
    path("busquedaEstudiantes/",busquedaEstudiantes,name="busquedaEstudiantes"),
    path("Cursos/",Cursos, name="Cursos"),
    path("CursosForm/",CursosForm, name="CursosForm"),
    path("busquedaCursos/",busquedaCursos,name="busquedaCursos"),
    path("ProfesoresForm/",ProfesoresForm, name="ProfesoresForm"),
    path("busquedaProfesores/",busquedaProfesor, name="busquedaProfesores"),
    # path("Formulario/",formulario, name="Formulario")
]

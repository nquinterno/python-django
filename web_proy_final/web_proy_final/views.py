from django.http import HttpResponse
from django.template import Template, Context, loader
from .models import * 
# from forms import *
from django.db.models import Q
from django.shortcuts import render
from .forms import *

# def inicio(request):
#     miHTML = open("./templates/home.html")
#     plantilla = Template(miHTML.read())
#     miHTML.close()
#     miContexto = Context()

#     documento = plantilla.render(miContexto)

#     return (HttpResponse(documento))

def inicio(request):
    # miContexto = Context()
    plantilla = loader.get_template('home.html')
    documento = plantilla.render()
    print("inicio")
    return (HttpResponse(documento))

def EstudiantesForm(request):
    if request.method == 'POST':
        estudiante = Estudiante(nombre = request.POST['Nombre'],apellido = request.POST['Apellido'],mail = request.POST['Email'])
        estudiante.save()
        return render(request,'web_proy_final/home.html')
    else:
        pass
    return render(request,'web_proy_final/EstudiantesForm.html')

def busquedaEstudiantes(request):
    if request.GET["busqueda"]:
        busqueda = Estudiante.objects.filter(Q(nombre__icontains = request.GET["busqueda"])|Q(apellido__icontains = request.GET["busqueda"])|Q(mail__icontains = request.GET["busqueda"]))
        if len(busqueda)>0:
            return render(request,"busquedaEstudiantes.html",{"busqueda": busqueda})
        else:
            return render(request,"busquedaEstudiantes.html",{"error":"No se han encontrado cursos con los datos suministrados"})

    else:
        busqueda = "No se enviaron datos para la busqueda"
    return HttpResponse(busqueda)

def Estudiantes(request):
    plantilla = loader.get_template('estudiantes.html')
    documento = plantilla.render()
    return (HttpResponse(documento))

def CursosForm(request):
    print("cursosform")
    if request.method == 'POST':
        print("post")
        miForm = cursoFormulario(request.POST)
        if miForm.is_valid():
            print("is valid")
            miForm_cleaned = miForm.cleaned_data
            print("cleaned")
            curso = Curso (numero_curso = miForm_cleaned['numero_curso'],tipo_curso = miForm_cleaned['tipo_curso'])
            curso.save()
            print("save")
            return render(request, 'web_proy_final/home.html')
    
    else:
        print("no post")
        miForm = cursoFormulario()

    return render(request, "CursosForm.html" ,{'miForm':miForm})

def busquedaCursos(request):

    if request.GET["busqueda"]:
        busqueda = Curso.objects.filter(Q(numero_curso__icontains = request.GET["busqueda"])|Q(tipo_curso__icontains = request.GET["busqueda"]))

        if len(busqueda)>0:
            return render(request,"busquedaCursos.html",{"busqueda": busqueda})
        else:
            return render(request,"busquedaCursos.html",{"error":"No se han encontrado cursos con los datos suministrados"})

    else:
        busqueda = "No se enviaron datos para la busqueda"
    return HttpResponse(busqueda)

def Cursos(request):
    plantilla = loader.get_template('cursos.html')
    documento = plantilla.render()
    return (HttpResponse(documento))

# def Profesores(request):
#     plantilla = loader.get_template('profesores.html')
#     documento = plantilla.render()
#     return (HttpResponse(documento))

def ProfesoresForm(request):
    if request.method == 'POST':
        profesor = Profesor(nombre = request.POST['nombre'], apellido = request.POST['apellido'], mail = request.POST['mail'])
        profesor.save()
        return render(request,'web_proy_final/home.html')
    else:
        pass
    return render(request,'web_proy_final/ProfesoresForm.html')

def busquedaProfesor(request):
    print("busqueda prof")
    if request.GET["busqueda"]:
        busqueda = Profesor.objects.filter(Q(nombre__icontains = request.GET["busqueda"])|Q(apellido__icontains = request.GET["busqueda"])|Q(mail__icontains = request.GET["busqueda"]))
        print(busqueda)
        print(len(busqueda))
        if len(busqueda)>0:
            return render(request,"busquedaProfesores.html",{"busqueda": busqueda})
        else:
            return render(request,"busquedaProfesores.html",{"error":"No se han encontrado cursos con los datos suministrados"})
    else:
        busqueda = "No se enviaron datos para la busqueda"
    return HttpResponse(busqueda)


# def cursoFormulario(request):
#     plantilla = loader.get_template('form_curso.html')
#     documento = plantilla.render()
#     return (HttpResponse(documento))

    

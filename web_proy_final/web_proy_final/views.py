from django.http import HttpResponse
from django.template import Template, Context, loader

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
    return (HttpResponse(documento))

    

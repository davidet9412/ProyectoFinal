from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from App1.models import *
from App1.forms import Pokemonform, Ataqueform, Tipoform

# Create your views here.


def inicio (request):
    
    pokemones = Pokemon.objects.all()

    return render (request,"App1/inicio.html", {'pokemones':pokemones})

def pokemonform(request):

    if request.method=="POST":
        form = Pokemonform(request.POST)

        if form.is_valid():
            info= form.cleaned_data
            nombre =  info["nombre"]
            tipo_1 =  info["tipo_1"]
            tipo_2 =  info["tipo_2"]
            ataque_1= info["ataque_1"]
            ataque_2= info["ataque_2"]
            ataque_3= info["ataque_3"]
            ataque_4= info["ataque_4"]
            id_pokedex= info["id_pokedex"]
            genero = info["genero"]
            pokemon = Pokemon(nombre=nombre,tipo_1=tipo_1,tipo_2=tipo_2,ataque_1=ataque_1,ataque_2=ataque_2,ataque_3=ataque_3,ataque_4=ataque_4,id_pokedex=id_pokedex,genero=genero)
            pokemon.save()
            form.clean()
            return render(request,"App1/pokemonform.html", {"pokemonform":form})
    
    else:
        form= Pokemonform()
    return render(request, "App1/pokemonform.html",{"pokemonform":form})

def ataqueform(request):

    if request.method=="POST":
        form = Ataqueform(request.POST)

        if form.is_valid():
            info= form.cleaned_data
            nombre =  info["nombre"]
            tipo =  info["tipo"]
            descripcion =  info["descripcion"]
            clase = info["clase"]          
            ataque = Ataque(nombre=nombre,tipo=tipo,descripcion=descripcion,clase=clase)
            ataque.save()
            form = Ataqueform()
            return render(request,"App1/ataqueform.html",{"ataqueform":form})
    
    else:
        form= Ataqueform()
    return render(request, "App1/ataqueform.html",{"ataqueform":form})

def tipoform(request):
    if request.method=="POST":
        form = Tipoform(request.POST)

        if form.is_valid():
            info= form.cleaned_data
            tipo_name =  info["tipo"]  
            tipo = Tipo(tipo=tipo_name)
            tipo.save()            
            form=Tipoform()
            return render(request,"App1/tipoform.html", {"tipoform":form})
    
    else:
        form= Tipoform()
    return render(request, "App1/tipoform.html",{"tipoform":form})

def busquedapokemon(request):
    return render(request,"App1/busquedapokemon.html" )


def buscar(request):
    if request.GET["pokemon"]:

        nombre = request.GET["pokemon"]
        pokemon = Pokemon.objects.filter(nombre = nombre)
        return render(request, "App1/resultadopokemon.html", {"pokemon":pokemon})

    else:
        return render(request, "App1/busquedapokemon.html", {"error":"No se ingreso ningun pokemon llamado ási "})


def resultadopokemon(request):

    pass 





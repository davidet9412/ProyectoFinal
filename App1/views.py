from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from App1.models import *
from App1.forms import Pokemonform, Ataqueform, Tipoform
from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import staff_member_required

from accounts.models import Post

# Create your views here.


def inicio (request):
    
    posts = Post.objects.all()   

    return render (request,"App1/inicio.html", {'posts':posts})

def about(request):

    return render(request,'App1/about.html')


@login_required
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

@staff_member_required
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

@staff_member_required
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


def leer_pokemon(request):

    pokemones = Pokemon.objects.all()

    return render(request, "App1/pokemones.html",{"pokemones": pokemones})

@login_required
def borrar_pokemon(request,nombre_pokemon):

    pokemon = Pokemon.objects.get(nombre=nombre_pokemon)
    pokemon.delete()

    pokemones = Pokemon.objects.all()

    return render(request,"App1/pokemones.html",{"pokemones": pokemones})

@login_required
def editar_pokemon(request,nombre_pokemon):

    pokemon = Pokemon.objects.get(nombre= nombre_pokemon)
    
    if request.method == 'POST':

        form = Pokemonform(request.POST)

        if form.is_valid():

            informacion = form.cleaned_data

            pokemon.nombre = informacion['nombre']
            pokemon.tipo_1 = informacion['tipo_1']            
            pokemon.tipo_2 = informacion['tipo_2']
            pokemon.ataque_1 = informacion['ataque_1']
            pokemon.ataque_2 = informacion['ataque_2']
            pokemon.ataque_3 = informacion['ataque_3']
            pokemon.ataque_4 = informacion['ataque_4']
            
            pokemon.save()

            return render(request,"App1/pokemones.html" )
    else:
            
        form= Pokemonform(initial={'nombre':pokemon.nombre,'tipo_1':pokemon.tipo_1,'tipo_2':pokemon.tipo_2,'ataque_1':pokemon.ataque_1,'ataque_2':pokemon.ataque_2,'ataque_3':pokemon.ataque_3,'ataque_4':pokemon.ataque_4})

    return render(request, 'App1/editarpokemon.html', {'formulario':form, 'nombre_pokemon':nombre_pokemon})




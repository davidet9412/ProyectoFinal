from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from posts.models import *
from posts.forms import Pokemonform, Ataqueform, PostEditForm, PostForm, Tipoform
from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import DetailView
from django.utils.text import slugify
from datetime import datetime
import uuid

from posts.models import Post

# Create your views here.


def inicio (request):
    
    posts = Post.objects.all()   

    return render (request,"posts/inicio.html", {'posts':posts})

def about(request):

    return render(request,'posts/about.html')


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
            return render(request,"posts/pokemonform.html", {"pokemonform":form})
    
    else:
        form= Pokemonform()
    return render(request, "posts/pokemonform.html",{"pokemonform":form})

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
            return render(request,"posts/ataqueform.html",{"ataqueform":form})
    
    else:
        form= Ataqueform()
    return render(request, "posts/ataqueform.html",{"ataqueform":form})

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
            return render(request,"posts/tipoform.html", {"tipoform":form})
    
    else:
        form= Tipoform()
    return render(request, "posts/tipoform.html",{"tipoform":form})

def busquedapokemon(request):
    return render(request,"posts/busquedapokemon.html" )


def buscar(request):
    if request.GET["pokemon"]:

        nombre = request.GET["pokemon"]
        pokemon = Pokemon.objects.filter(nombre = nombre)
        return render(request, "posts/resultadopokemon.html", {"pokemon":pokemon})

    else:
        return render(request, "posts/busquedapokemon.html", {"error":"No se ingreso ningun pokemon llamado ási "})


def resultadopokemon(request):

    pass 


def leer_pokemon(request):

    pokemones = Pokemon.objects.all()

    return render(request, "posts/pokemones.html",{"pokemones": pokemones})

@login_required
def borrar_pokemon(request,nombre_pokemon):

    pokemon = Pokemon.objects.get(nombre=nombre_pokemon)
    pokemon.delete()

    pokemones = Pokemon.objects.all()

    return render(request,"posts/pokemones.html",{"pokemones": pokemones})

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

            return render(request,"posts/pokemones.html" )
    else:
            
        form= Pokemonform(initial={'nombre':pokemon.nombre,'tipo_1':pokemon.tipo_1,'tipo_2':pokemon.tipo_2,'ataque_1':pokemon.ataque_1,'ataque_2':pokemon.ataque_2,'ataque_3':pokemon.ataque_3,'ataque_4':pokemon.ataque_4})

    return render(request, 'posts/editarpokemon.html', {'formulario':form, 'nombre_pokemon':nombre_pokemon})


@login_required
def crear_post(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user = request.user
            slug = slugify(str(uuid.uuid4()))
            post = form.save(commit=False)
            post.slug = slug
            post.autor = user
            publish = form.cleaned_data.get("publicado", False)
            if publish:
                post.fecha_publicacion = datetime.now()
            post.save()
            return redirect(f"/posts/{post.pk}")
        
        else:
            print(form.errors)
    
    else:
        form= PostForm()
    return render(request, "posts/post_form.html",{"form":form, "action": "crear_post"})

@login_required
def editar_post(request, slug):
    post = Post.objects.get(slug=slug)
    was_published = post.publicado
    if request.method=="POST":
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            if was_published and not post.publicado:
                post.fecha_publicacion = None
            if not was_published and post.publicado:
                post.fecha_publicacion = datetime.now() 

            post.save()
            return redirect(f"/posts/{post.pk}")
    else:
        form = PostEditForm(instance=post)
    return render(request, "posts/post_edit_form.html",{"form":form, "slug": slug})

class ArticleDetailView(DetailView):
    model = Post
    template_name= 'accounts/post_details.html'
from django.contrib import admin
from django.urls import path
from posts.views import *


urlpatterns = [
    path("pokemonform/", pokemonform, name="pokemonform"),
    path("ataqueform/", ataqueform, name="ataqueform"),
    path("tipoform/", tipoform, name="tipoform"),
    path("buscar/", buscar, name="buscar"),
    path("busquedapokemon/", busquedapokemon, name="busquedapokemon"),
    path("resultadopokemon/", resultadopokemon, name="resultadopokemon"),
    path("pokemones/", leer_pokemon, name="leer_pokemon"),
    path("editarpokemon/<pokemon_nombre>", editar_pokemon, name="editar_pokemon"),
    path("create/", crear_post, name="crear_post"),
    path("edit/<uuid:slug>/", editar_post, name="editar_post"),
    path("<uuid:pk>/", ArticleDetailView.as_view(), name="post_details"),
]

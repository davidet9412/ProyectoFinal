from django.contrib import admin
from django.urls import path
from App1.views import *


urlpatterns = [
    path('',inicio, name='inicio'),
    path('pokemonform/', pokemonform, name= 'pokemonform'),
    path('ataqueform/', ataqueform, name= 'ataqueform'),
    path('tipoform/', tipoform, name= 'tipoform'),
    path('buscar/', buscar, name="buscar"),
    path('busquedapokemon/', busquedapokemon, name='busquedapokemon'),
    path('resultadopokemon/',resultadopokemon, name= 'resultadopokemon'),
]

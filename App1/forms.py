from email.policy import default
from django import forms
from numpy import empty

from App1.models import Tipo, Ataque


class Pokemonform(forms.Form):

    Hombre = "H"
    Mujer = "M"    
    genero_options = [(Hombre,"H"),(Mujer,"M")]
    nombre =  forms.CharField(max_length=50)
    tipo_1 =  forms.ModelChoiceField(queryset=Tipo.objects.all(),empty_label=None)
    tipo_2 =  forms.ModelChoiceField(queryset=Tipo.objects.all(),empty_label="",required=False)
    ataque_1= forms.ModelChoiceField(queryset=Ataque.objects.all(),empty_label=None)
    ataque_2= forms.ModelChoiceField(queryset=Ataque.objects.all(),empty_label="",required=False)
    ataque_3= forms.ModelChoiceField(queryset=Ataque.objects.all(),empty_label="",required=False)
    ataque_4= forms.ModelChoiceField(queryset=Ataque.objects.all(),empty_label="",required=False)


class Ataqueform(forms.Form):

    Ataque_fisico = "Fisico"
    Ataque_especial = "Especial"
    clase_ataque = [(Ataque_fisico,"Fisico"),(Ataque_especial, "Especial")]

    nombre= forms.CharField(max_length=50)
    clase= forms.ChoiceField(choices=clase_ataque)
    tipo= forms.ModelChoiceField(queryset=Tipo.objects.all(),empty_label=None)
    descripcion= forms.CharField(max_length=9999,required=False)

class Tipoform(forms.Form):
    tipo = forms.CharField(max_length=30)
   
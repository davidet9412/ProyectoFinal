from django import forms

class Pokemonform(forms.Form):

    Hombre = "H"
    Mujer = "M"    
    genero_options = [(Hombre,"H"),(Mujer,"M")]
    nombre =  forms.CharField(max_length=50)
    tipo_1 =  forms.CharField(max_length=50)
    tipo_2 =  forms.CharField(max_length=50)
    ataque_1= forms.CharField(max_length=50)
    ataque_2= forms.CharField(max_length=50)
    ataque_3= forms.CharField(max_length=50)
    ataque_4= forms.CharField(max_length=50)
    id_pokedex= forms.IntegerField()
    genero = forms.ChoiceField(choices=genero_options)


class Ataqueform(forms.Form):

    Ataque_fisico = "Fisico"
    Ataque_especial = "Especial"
    clase_ataque = [(Ataque_fisico,"Fisico"),(Ataque_especial, "Especial")]

    nombre= forms.CharField(max_length=50)
    clase= forms.ChoiceField(choices=clase_ataque)
    tipo= forms.CharField(max_length=50)
    descripcion= forms.CharField(max_length=9999)

class Tipoform(forms.Form):
    tipo_1 = forms.CharField(max_length=30)
    tipo_2 = forms.CharField(max_length=30)
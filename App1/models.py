from django.db import models

# Create your models here.

class Pokemon(models.Model):
    
    Hombre = "H"
    Mujer = "M"    
    genero_options = [(Hombre,"H"),(Mujer,"M")]
    nombre = models.CharField(max_length=50)
    tipo_1 = models.CharField(max_length=50)
    tipo_2 = models.CharField(max_length=50)
    ataque_1= models.CharField(max_length=50)
    ataque_2= models.CharField(max_length=50)
    ataque_3= models.CharField(max_length=50)
    ataque_4= models.CharField(max_length=50)
    id_pokedex= models.IntegerField()
    genero = models.CharField(max_length=1, choices=genero_options)

    def __str__(self) -> str:
        return self.nombre

class Region(models.Model):

    nombre = models.CharField(max_length=30)


class Ataque(models.Model):

    Ataque_fisico = "Fisico"
    Ataque_especial = "Especial"
    clase_ataque = [(Ataque_fisico,"Fisico"),(Ataque_especial, "Especial")]

    nombre= models.CharField(max_length=50)
    clase= models.CharField(max_length=8, choices=clase_ataque)
    tipo= models.CharField(max_length=50)
    descripcion= models.CharField(max_length=9999)


class Tipo(models.Model):
    tipo_1 = models.CharField(max_length=30)
    tipo_2 = models.CharField(max_length=30)
    
from pickle import TRUE
from django.db import models


# Create your models here.

class Pokemon(models.Model):
    
    Hombre = "H"
    Mujer = "M"    
    genero_options = [(Hombre,"H"),(Mujer,"M")]
    nombre = models.CharField(max_length=50)
    tipo_1 = models.ForeignKey("Tipo",on_delete=models.PROTECT, related_name="tipo_1")
    tipo_2 = models.ForeignKey("Tipo",on_delete=models.PROTECT, related_name="tipo_2",null=True,blank=True)
    ataque_1= models.ForeignKey("Ataque",on_delete=models.SET_NULL,null=True,related_name="ataque_1")
    ataque_2= models.ForeignKey("Ataque",on_delete=models.SET_NULL,null=True,related_name="ataque_2",blank=True)
    ataque_3= models.ForeignKey("Ataque",on_delete=models.SET_NULL,null=True,related_name="ataque_3",blank=True)
    ataque_4= models.ForeignKey("Ataque",on_delete=models.SET_NULL,null=True,related_name="ataque_4",blank=True)


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
    tipo= models.ForeignKey("Tipo",on_delete=models.PROTECT)
    descripcion= models.CharField(max_length=9999)

    def __str__(self):
        return self.nombre


class Tipo(models.Model):
    tipo = models.CharField(max_length=30)    

    def __str__(self):
        return self.tipo
    
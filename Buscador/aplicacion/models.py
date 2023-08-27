from django.db import models



class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    abreviacion=models.CharField(max_length=4,null=True)

class Fuerza(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE,null=False)

class Regimiento(models.Model):
    nombre = models.CharField(max_length=100)
    fuerza = models.ForeignKey(Fuerza, on_delete=models.CASCADE,null=False)
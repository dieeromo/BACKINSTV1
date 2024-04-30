from django.db import models

from django.db import models

from accounts.models import UserAccount

class TipoInventario(models.Model): 
    tipo = models.CharField(max_length=255)
    # Fungible, no fungible


class EstadoInventario(models.Model): 
    estado = models.CharField(max_length=255)
    #Bueno, malo, regular


class UbicacionInventario(models.Model): 
    ubicacion = models.CharField(max_length=400)
    # Rectorado, Lab1, Lab 2
    referencia = models.CharField(max_length=400, blank=True, null= True)
    # #ubicado junto a xxx

class InventarioIST(models.Model): 
    cod_unico = models.CharField(max_length=200) #codigo unico del sistema, este se lo pone al momento de registrar el equipo al sistema
    cod_senescyt = models.CharField(max_length=200, null=True, blank=True) #codigo asignado por senesvcyt, o si el usuario no ingresa nada, el sistema le pone automaticamente NA
    cod_instituto = models.CharField(max_length=200,null=True, blank=True) #codigo asignado por el institutp, o si el usuario no ingresa nada, el sistema le pone automaticamente NA
    tipo = models.ForeignKey(TipoInventario,on_delete=models.CASCADE)
    descripcion = models.TextField()
    materiales = models.TextField()
    marca = models.CharField(max_length=200, null=True, blank=True) # va la marca o si el usuario no ingresa nada, el sistema le pone automaticamente NA
    modelo = models.CharField(max_length=200, null=True, blank=True) # va el modelo o si el usuario no ingresa nada, el sistema le pone automaticamente NA
    serie = models.CharField(max_length=200, null=True, blank=True) # va la serie o si el usuario no ingresa nada, el sistema le pone automaticamente NA
    color = models.CharField(max_length=200) 

    estado = models.ForeignKey(EstadoInventario,on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(UbicacionInventario,on_delete=models.CASCADE)
    asignado = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name ='digitador1',null=True, blank=True)
    observacion = models.TextField(null=True, blank= True)


from django.db import models
from django.conf import settings
from django.utils import timezone 

# Create your models here.
class Suscripciones(models.Model):
    numero_de_cuenta=models.CharField(max_length=50,null=False)
    ENTIDADES=[('CA','“Caixa”'),('BB','“BBVA”'),('UN','“UNICAJA”'),('IN','”ING”')]
    entidad_bancaria=models.CharField(max_length=2,choices=ENTIDADES,null=False)

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50,blank=True)
    SEXO=[('M','Masculino'),('F','Femenino')]
    sexo=models.CharField(max_length=1,choices=SEXO)
    fecha_nacimiento=models.DateField()
    codigo_postal=models.IntegerField()
    domicilio=models.TextField()
    correo= models.EmailField(max_length=50)
    telefono=models.PositiveIntegerField()
    dni=models.CharField(max_length=9,unique=True)
    #RELACIONES
    suscripcion=models.OneToOneField(Suscripciones,on_delete=models.CASCADE,null=True,related_name="cliente_Suscripciones")
    
class Vivienda(models.Model):
    localidad=models.CharField(max_length=50)
    calle=models.CharField(max_length=50)
    numero=models.PositiveIntegerField()
    metros_cuadrados=models.FloatField()
    propietario=models.CharField(max_length=50)
    precio=models.FloatField(editable=True)
    #Relaciones
    cliente=models.ManyToManyField(Cliente,related_name='vivienda_Cliente')
    votacion= models.ManyToManyField(Cliente, through='Votacion',related_name="vivienda_Votacion")
    
class Votacion(models.Model):
    puntuacion=models.PositiveIntegerField(default=0)
    comentario=models.TextField()
    fecha_votacion=models.DateField(default=timezone.now)
    #RELACIONES
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,related_name="votacion_Cliente")
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE,related_name="votacion_Vivienda")
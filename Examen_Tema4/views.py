from django.shortcuts import render
from .models import *
from django.db.models import Q,Prefetch, Count

# Create your views here.
def index(request):
    return render(request,"index.html")

# El último voto que se realizó en un modelo principal en concreto, 
# y mostrar el comentario, la votación e información del usuario o 
# cliente que lo realizó: 1.5 puntos
def ultimo_voto(request):
    voto=Votacion.objects.select_related("cliente","vivienda")
    voto=voto.order_by("-fecha_votacion")[:1].get()
    return render(request,"Votos/ultimo_voto.html",{'views_ultimo_voto':voto})

# Todos los modelos principales que tengan votos con una puntuación numérica 
# menor a 3 y que realizó un usuario o cliente en concreto: 1.5 puntos
def viviendas_puntuacion(request,id_cliente):
    viviendas=Vivienda.objects.prefetch_related("cliente",Prefetch("votacion_Vivienda"))
    viviendas=viviendas.filter(votacion_Vivienda__cliente__id=id_cliente,votacion_Vivienda__puntuacion__lte=3).all()
    return render(request,"Viviendas/viviendas_puntuacion.html",{'views_viviendas_puntuacion':viviendas})

# Todos los usuarios o clientes que no han votado nunca y mostrar 
# información sobre estos usuarios y clientes al completo: 1.5 puntos
def clientes_nunca_votado(request):
    clientes=Cliente.objects.select_related("suscripcion").prefetch_related(Prefetch("vivienda_Cliente"),Prefetch("votacion_Cliente"))
    clientes=clientes.filter(votacion_Cliente=None).all()
    return render(request,"Clientes/clientes_nunca_votado.html",{'views_clientes_nunca_votado':clientes})

# Obtener las cuentas bancarias que sean de la Caixa o de Unicaja y que el propietario 
# tenga un nombre que contenga un 
# texto en concreto, por ejemplo “Juan”: 1.5 puntos
def cuentasbancarias(request,contiene):
    cuentas=Suscripciones.objects.prefetch_related(Prefetch("cliente_Suscripciones"))
    cuentas=cuentas.filter((Q(entidad_bancaria="CA") | Q(entidad_bancaria="UN")),cliente_Suscripciones__nombre__contains=contiene).all()
    return render(request,"Cuentas/cuentasbancarias.html",{'views_cuentasbancarias':cuentas})
 
# Obtener los votos de los usuarios que hayan votado a partir del 2023 con una puntuación numérica igual
# a 5  y que tengan asociada una cuenta bancaria. 1.5 puntos
def votos_usuarios(request):
    voto=Votacion.objects.select_related("cliente","vivienda")
    voto=voto.filter(fecha_votacion__year__gt=2023,puntuacion__gt=4,puntuacion__lt=6,cliente__suscripcion=not None).all()
    return render(request,"Votos/votos_usuarios.html",{'views_votos_usuarios':voto}) 


def mi_error_400(request,exception=None):
    return render(request,"errores/400.html",None,None,400)
def mi_error_403(request,exception=None):
    return render(request,"errores/403.html",None,None,403)
def mi_error_404(request,exception=None):
    return render(request,"errores/404.html",None,None,404)
def mi_error_500(request,exception=None):
    return render(request,"errores/500.html",None,None,500)
from django.urls import path
from django.contrib import admin
from .import views

# AQUI VAN LAS URLS

urlpatterns = [
    path('', views.index,name="urls_index"),
    #1
    path('Votos/ultimo_voto', views.ultimo_voto,name="urls_ultimo_voto"),
    #2
    path('Viviendas/viviendas_puntuacion/<int:id_cliente>', views.viviendas_puntuacion,name="urls_viviendas_puntuacion"),
    #3
    path('Clientes/clientes_nunca_votado', views.clientes_nunca_votado,name="urls_clientes_nunca_votado"),
    #4
    path('Cuentas/cuentasbancarias/<str:contiene>', views.cuentasbancarias,name="urls_cuentasbancarias"), 
    #5
    path('Votos/votos_usuarios', views.votos_usuarios,name="urls_votos_usuarios"), 
]
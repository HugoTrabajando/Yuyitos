###este archivo tiene todas las rutas de la pagina web
##es necesario. Fue copiado del proyecto_toreto/urls.py

from django.contrib import admin
from django.urls import include, path
##escribir un from de las views.py
from .views import cerrar_sesion, index, logear, registro, test

###rutas redireccionar las paginas
urlpatterns = [
    path('test', test,name='TEST'), ##pagina testing
    path('', index,name='INDEX'), ##pagina index si no se escribe nada

    path('logear/',logear,name="LOGEAR"),
    path('registro/',registro,name="REGISTRO"),
    path('cerrar/',cerrar_sesion,name='CERRAR'),

    #path('registrar_cliente/',registrar_cliente,name='REGISTRAR_CLIENTE'),
    #path('modificar_cliente/',modificar_cliente,name='MODIFICAR_CLIENTE'),
    #path('modificar_cliente/<id_client>/',reg_cli_modificar,name='MODI_CLIENTE'),
    #path('eliminar_cliente/<id_client>/',reg_cli_eliminar,name='ELIMINAR_CLIENTE'),

]

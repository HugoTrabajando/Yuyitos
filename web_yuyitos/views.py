from django.contrib import auth
from django.db.models.fields.mixins import FieldCacheMixin
from django.db import reset_queries
from django.http import response
from datetime import datetime
from django.shortcuts import render
from .models import Tecnico, Cliente, Repuesto, Proveedor, Atencion_hora, Servicio, Order_repuesto, Galeria, Vehiculo
# importar el modelo de usuarios
from django.contrib.auth.models import User
# importar librerias de acceso a login
from django.contrib.auth import authenticate,logout,login as login_aut
# importar libreria de decorador para impedir el acceso a las paginas
from django.contrib.auth.decorators import login_required,permission_required


# Create your views here.
####segun, se debe crear metodos para asi funcionen en urls.py
####debo renderizar paginas, creando metodos aca

###testing
def test(request):
    return render(request, "./test.html")
###fin testing

def index(request):
    return render(request, "./index.html")

def logear(request):
    if request.POST:
        usuario = request.POST.get("txtuser")
        contra = request.POST.get("txtcontrasena")
        us = authenticate(request,username=usuario,password=contra)
        if us is not None and us.is_active:
            login_aut(request,us)
            tipos = Tecnico.objects.all()
            contexto ={"tipos":tipos}
            return render(request, "index.html",contexto)          
        else:
            contexto = {"mensaje":"Usuario o contraseña incorrecto"}
            return render(request,"login.html",contexto)
    return render(request,"login.html")

##REGISTRO / SIGN IN DE PAGINA
def registro(request):
    ##return render(request,"registro.html")
    mensaje=""
    if request.POST:
        nombre = request.POST.get("txtnombre")
        nom_usuario = request.POST.get("txtusuario")
        email = request.POST.get("txtcorreo")
        pass1 = request.POST.get("txtcontrasena")
        passok = request.POST.get("txtcontrasenaok")

        if pass1!=passok:
            mensaje="contraseñas no son iguales"
            contexto= {"mensaje":mensaje}
            return render(request,"registro.html",contexto)        

        usu = User()
        usu.first_name = nombre
        ##--usu.last_name = apellido
        usu.email = email
        usu.username = nom_usuario
        usu.set_password(pass1)
        usu.save()
        mensaje="Se ha guardado esta creación de usuario!"

    contexto={"mensaje":mensaje}
    return render(request,"registro.html",contexto)

##cierre de sesion
def cerrar_sesion(request):
    logout(request)
    tipos = Tecnico.objects.all()
    contexto ={"tipos":tipos}
    return render(request, "index.html",contexto)

##exclusivo solo para logeados
##Esto cada vez que es escrito, afecta al DEF de abajo, no de arriba....
######estas variables pueden servir ante emergencia de errores
###usuario1 = User().username
fecha_ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
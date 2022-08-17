from django.shortcuts import render
from .models import *

# Create your views here.

def holamundocore (request) :
    return render (request, 'core.html')

def nosotros (request) :
    ports2 = persona.objects.all()
    return render (request,'nosotros.html', context= {'Ports': ports2})

def productos (request) :
    ports4 = maquina.objects.all()
    return render(request, 'productos.html' , context= {'Ports': ports4})

def contactanos (resquest) :
    return  render( resquest, 'contactanos.html')

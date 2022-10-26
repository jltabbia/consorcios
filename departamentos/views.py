import json
from django.shortcuts import render,redirect
from django.core import serializers
from django.views.generic import View
from django.http import HttpResponse
from .forms import DepartamentoForm
from modelos.models import Departamentos, Edificios


# Create your views here.

class DepartamentosHomeView(View):
    def get(self,request,*args,**kwargs):
        edificios=Edificios.objects.filter(administrador=request.user)
        return render(request,'departamentos/index.html',{'edificios':edificios})

class crear(View):
     def get(self,request,*args,**kwargs):
         form = DepartamentoForm()
         context = {
             'form':form,
         }
         return render(request,'departamentos/crear.html',context=context)
     def post(self,request,*args,**kwargs):
         form = DepartamentoForm(request.POST)
         if form.is_valid():
             propietario = form.save()
             form = DepartamentoForm()
         return redirect('/departamentos/')

def listarDptos(request):
    edi=request.GET.get("edi")
    dptos=Departamentos.objects.all().filter(edificio_id=edi).select_related('propietario')
    
    dptos=[dptos_serializer(dpto) for dpto in dptos]
 
    return HttpResponse(json.dumps(dptos), content_type='application/json')

def dptos_serializer(dpto):
    return {'piso': dpto.piso, 'numero': dpto.numero, 'propietario': dpto.propietario.nombre+" "+dpto.propietario.apellido , 'porcentaje': dpto.porcentaje}



    
    
    
        
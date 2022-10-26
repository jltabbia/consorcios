from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import PropietarioForm
from modelos.models import Propietarios

# Create your views here.

class PropietariosHomeView(View):
    def get(self,request,*args,**kwargs):
        propietarios=Propietarios.objects.all()
        
        return render(request,'propietarios/index.html',{'propietarios':propietarios})
    

class crear(View):
    #if request.method == "GET":
    def get(self,request,*args,**kwargs):
        form = PropietarioForm()
        context = {
            'form':form
        }
        return render(request,'propietarios/crear.html',context=context)
    def post(self,request,*args,**kwargs):
        form = PropietarioForm(request.POST)
        if form.is_valid():
            propietario = form.save()
            form = PropietarioForm()
        return redirect('/propietarios/')

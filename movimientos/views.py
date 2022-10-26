from tkinter import MOVETO
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import MovimientoForm
from modelos.models import Movimientos
# Create your views here.


class MovimientosHomeView(View):
    def get(self,request,*args,**kwargs):
        movimientos=Movimientos.objects.all()
        
        return render(request,'movimientos/index.html',{'movimientos':movimientos})
    

class crear(View):
    #if request.method == "GET":
    def get(self,request,*args,**kwargs):
        form = MovimientoForm()
        context = {
            'form':form
        }
        return render(request,'movimientos/crear.html',context=context)
    def post(self,request,*args,**kwargs):
        form = MovimientoForm(request.POST)
        if form.is_valid():
            propietario = form.save()
            form = MovimientoForm()
        return redirect('/movimientos/')

from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import EdificoForm
from modelos.models import Edificios

# Create your views here.

class EdificiosHomeView(View):
    def get(self,request,*args,**kwargs):
        edificios=Edificios.objects.filter(administrador=request.user)
        
        return render(request,'edificios/index.html',{'edificios':edificios})
    

class crear(View):
    #if request.method == "GET":
    def get(self,request,*args,**kwargs):
        form = EdificoForm()
        context = {
            'form':form
        }
        return render(request,'edificios/crear.html',context=context)
    def post(self,request,*args,**kwargs):
        form = EdificoForm(request.POST)
        if form.is_valid():
            edificio = form.save()
            form = EdificoForm()
        return redirect('/edificios/')

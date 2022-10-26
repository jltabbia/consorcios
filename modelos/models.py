from random import choices
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
from django.db import models
from usuarios.models import Usuario

# definimos modelo Propietarios
class Propietarios(models.Model):
    # id=models.IntegerField(primary_key=True,serialize=True)
    nombre=models.CharField(max_length=45,verbose_name="Nombre")
    apellido=models.CharField(max_length=45,verbose_name="Apellido")
    domicilio=models.CharField(max_length=45, verbose_name="Domicilio",blank=True,null=True)
    contacto=models.CharField(max_length=15,verbose_name="Tel. de Contacto",blank=True,null=True)
    email=models.EmailField(verbose_name="Correo Electrónico",blank=True,null=True)
    cuit_cuil=models.CharField(max_length=15,blank=False, null=False,verbose_name="CUIT/CUIL")
    
    def __str__ (self):
       return '%s %s' % (self.nombre, self.apellido)
    
    class Meta:
        db_table = 'propietarios'
        ordering = ["apellido","nombre"]
        verbose_name_plural = "Propietarios"
        verbose_name = 'Propietario'
        managed=True
        
# definimos modelo Edificios
class Edificios(models.Model):
    nombre=models.CharField(max_length=45,verbose_name="Nombre Edificio")
    domicilio=models.CharField(max_length=45, verbose_name="Domicilio")
    cantidad_dptos=models.IntegerField(default=0)
    administrador=models.ForeignKey("usuarios.Usuario", verbose_name= ("Administrador"), on_delete=models.CASCADE)

    def __str__ (self):
        return self.nombre
    
    class Meta:
        db_table = 'edificios'
        ordering = ["nombre"]
        verbose_name = "Edificio"
        verbose_name_plural = "Edificios"

# definimos modelo Departamentos
class Departamentos(models.Model):
    piso=models.IntegerField(verbose_name="Nro. de Piso")
    numero=models.CharField(max_length=2,blank=False, null=False,verbose_name="Nro. Departamento")
    propietario=models.ForeignKey("propietarios",verbose_name="Propietario",on_delete=models.CASCADE)
    edificio=models.ForeignKey("edificios",verbose_name="Edificio", on_delete=models.CASCADE)
    porcentaje=models.FloatField(verbose_name="Porcentaje expensas")

    def __str__(self):
        return self.id,self.piso,self.numero,self.porcentaje
    
    class Meta:
        db_table='departamentos'
        ordering = ["id"]
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        managed=True

# definimos modelo Movimientos
EXPENSAS = (
    ("S","Corresponde"),
    ("N","No Corresponde"),
)

class Movimientos(models.Model):
    mes=models.IntegerField(blank=False, null=False)
    anio=models.IntegerField(blank=False, null=False)
    tipo_movimiento=models.CharField(max_length=1, blank=False, null=False)
    fecha_movimiento=models.DateField(blank=False, null=False)
    detalle=models.CharField(max_length=100,null=False,blank=False)
    importe=models.FloatField(default=0)
    comprobante=models.CharField(max_length=50,blank=True,null=True)
    expensas=models.CharField(max_length=1, blank=False, null=False, choices=EXPENSAS)    
    
    def __str__(self):
        return super().__str__()
    
    class Meta:
        db_table="movimientos"
        ordering=["id"]
        verbose_name="Movimientos"
        verbose_name_plural="Movimientos"
        
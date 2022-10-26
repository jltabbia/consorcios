from django.urls import path
from .views import *

app_name='movimientos'

urlpatterns = [
    path('', MovimientosHomeView.as_view(), name='index'),
    path('crear',crear.as_view(),name="crear"),
    # path('eliminar/<int:id>', eliminar),
    # path('editar/<int:id>',editar),

]
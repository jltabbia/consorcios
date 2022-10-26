from django.urls import path
from .views import *

app_name='edificios'

urlpatterns = [
    path('', EdificiosHomeView.as_view(), name='index'),
    path('crear',crear.as_view(),name="crear"),
    # path('eliminar/<int:id>', eliminar),
    # path('editar/<int:id>',editar),

]
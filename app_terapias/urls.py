from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='lista_terapias'),
    path('<int:id>/', views.ver_terapia, name='ver_terapia'),
    path('agregar/', views.agregar_terapia, name='agregar_terapia'),
    path('editar/<int:id>/', views.editar_terapia, name='editar_terapia'),
    path('borrar/<int:id>/', views.borrar_terapia, name='borrar_terapia'),
]

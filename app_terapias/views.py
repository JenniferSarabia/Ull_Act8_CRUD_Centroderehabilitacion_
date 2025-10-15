from django.shortcuts import render, redirect, get_object_or_404
from .models import Terapia

# Listar terapias
def index(request):
    terapias = Terapia.objects.all()
    return render(request, 'listar_terapias.html', {'terapias': terapias})

# Ver terapia (opcional, puedes usarlo si quieres detalle)
def ver_terapia(request, id):
    terapia = get_object_or_404(Terapia, id=id)
    return render(request, 'ver_terapia.html', {'terapia': terapia})

# Agregar terapia
def agregar_terapia(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        duracion = request.POST['duracion']
        cita = request.POST['cita']
        Terapia.objects.create(nombre=nombre, descripcion=descripcion, duracion=duracion, cita=cita)
        return redirect('lista_terapias')
    return render(request, 'agregar_terapia.html')

# Editar terapia
def editar_terapia(request, id):
    terapia = get_object_or_404(Terapia, id=id)
    if request.method == 'POST':
        terapia.nombre = request.POST['nombre']
        terapia.descripcion = request.POST['descripcion']
        terapia.duracion = request.POST['duracion']
        terapia.cita = request.POST['cita']
        terapia.save()
        return redirect('lista_terapias')
    return render(request, 'editar_terapia.html', {'terapia': terapia})

# Borrar terapia
def borrar_terapia(request, id):
    terapia = get_object_or_404(Terapia, id=id)
    if request.method == 'POST':
        terapia.delete()
        return redirect('lista_terapias')
    return render(request, 'borrar_terapia.html', {'terapia': terapia})

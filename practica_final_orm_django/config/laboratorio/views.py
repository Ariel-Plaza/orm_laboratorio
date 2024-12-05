from django.shortcuts import render, redirect, get_object_or_404
from .models import Laboratorio

def mostrar_laboratorio(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorio/ver_laboratorios.html', {'laboratorios': laboratorios})

def crear_laboratorio(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ciudad = request.POST.get('ciudad')
        pais = request.POST.get('pais')
        Laboratorio.objects.create(nombre=nombre, ciudad=ciudad, pais=pais)
        return redirect('laboratorio:laboratorio_index')

def editar_laboratorio(request, pk):
    laboratorio = get_object_or_404(Laboratorio, id=pk)
    if request.method == 'POST':
        laboratorio.nombre = request.POST.get('nombre')
        laboratorio.ciudad = request.POST.get('ciudad')
        laboratorio.pais = request.POST.get('pais')
        laboratorio.save()
        return redirect('laboratorio:laboratorio_index')

def eliminar_laboratorio(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    laboratorio.delete()
    return redirect('laboratorio:laboratorio_index')




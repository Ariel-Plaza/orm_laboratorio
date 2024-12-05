from .import views
from django.urls import path

app_name = 'laboratorio'

urlpatterns = [
    path('', views.mostrar_laboratorio, name='laboratorio_index'),
    path('crear_laboratorio/', views.crear_laboratorio, name="crear_laboratorio"),
    # path('editar_laboratorio/', views.editar_laboratorio, name="editar_laboratorio")
    path('editar_laboratorio/<int:pk>', views.editar_laboratorio, name="editar_laboratorio"),
    path('eliminar_laboratorio/<int:pk>', views.eliminar_laboratorio, name="eliminar_laboratorio"),

]
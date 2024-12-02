from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto
import  datetime
from django.db.models import IntegerField

from django import forms

# Register your models here.
@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
        list_display = ("id", "nombre")

@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "laboratorio")

# id,nombre, laboratorio

class ProductoAdmin(admin.ModelAdmin):
    fields = ('nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    list_display = ("id", "nombre", "laboratorio", "fabricacion_year", "p_costo", "p_venta")

    def fabricacion_year(self, obj):
        if obj.f_fabricacion:
            return obj.f_fabricacion.year
        else:
            return "-"
    fabricacion_year.short_description = "f_fabricacion"
    list_filter = ("nombre", "laboratorio")

# Registramos el modelo Producto en el admin
admin.site.register(Producto, ProductoAdmin)
  
  
  
  
        
# @admin.register(Producto) 
# class ProductoAdmin(admin.ModelAdmin): 
#     fields = ('nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta') 
#     list_display = ("id", "nombre", "laboratorio", "fabricacion_year", "p_costo", "p_venta") 
    
#     def fabricacion_year(self, obj): 
#         if obj.f_fabricacion: 
#             return obj.f_fabricacion.year 
#         else: 
#             return "-" 
#     fabricacion_year.short_description = "f_fabricacion" 
#     list_filter = ("nombre", "laboratorio")
    
# class ProductoAdmin(admin.ModelAdmin):
#     form = ProductoForm

# admin.site.register(Producto, ProductoAdmin)
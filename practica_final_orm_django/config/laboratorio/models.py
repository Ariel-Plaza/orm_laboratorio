import datetime
from turtle import mode
from django.db import models
from django.core.validators  import MinValueValidator
from django.utils.timezone import make_aware

# Create your models here.

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=25, default='Santiago')
    pais = models.CharField(max_length=25, default='Chile')

    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=50, default='Sin especialidad')
    
    def __str__(self):
        return f'{self.nombre},{self.laboratorio}'

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateTimeField(
        validators=[
            MinValueValidator(make_aware(datetime.datetime(2015, 1, 1, 0, 0)))
        ]
    )
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta =  models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return  f'{self.nombre}'


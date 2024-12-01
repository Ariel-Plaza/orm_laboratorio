import datetime
from django.db import models
from django.core.validators  import MinValueValidator

# Create your models here.

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Director General: {self.nombre}, Laboratorio: {self.laboratorio}'

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateTimeField(validators=[MinValueValidator(datetime.date(2015,1,1))])
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta =  models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'Producto: {self.nombre}, Laboratorio: {self.laboratorio}, Valor Venta: {self.p_venta}.'


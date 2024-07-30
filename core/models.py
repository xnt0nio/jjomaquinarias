from django.db import models
from django.core.exceptions import ValidationError

class TipoProducto(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=250)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(blank=True)
    vigente = models.BooleanField()
    
    marca = models.CharField(max_length=50, null=True, blank=True)
    modelo = models.CharField(max_length=50, null=True, blank=True)
    motor = models.CharField(max_length=100, null=True, blank=True)
    potencia = models.CharField(max_length=100, null=True, blank=True)
    traccion = models.CharField(max_length=10, null=True, blank=True)
    alimentacion = models.CharField(max_length=20, null=True, blank=True)
    neumaticos = models.CharField(max_length=20, null=True, blank=True)
    caracteristica = models.TextField(null=True, blank=True)
    equipamiento = models.TextField(null=True, blank=True)

    def clean(self):
        if self.potencia is not None and self.potencia < 0:
            raise ValidationError('La potencia no puede ser negativa')
        if self.marca and len(self.marca) > 50:
            raise ValidationError('La marca no puede tener más de 50 caracteres')
        if self.modelo and len(self.modelo) > 50:
            raise ValidationError('El modelo no puede tener más de 50 caracteres')
        if self.motor and len(self.motor) > 100:
            raise ValidationError('El motor no puede tener más de 100 caracteres')
        if self.traccion and len(self.traccion) > 10:
            raise ValidationError('La tracción no puede tener más de 10 caracteres')
        if self.alimentacion and len(self.alimentacion) > 20:
            raise ValidationError('La alimentación no puede tener más de 20 caracteres')
        if self.neumaticos and len(self.neumaticos) > 20:
            raise ValidationError('Los neumáticos no pueden tener más de 20 caracteres')

    def __str__(self):
        return self.nombre
    

class mensaje(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.asunto}"     
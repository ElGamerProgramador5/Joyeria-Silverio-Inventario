from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    material = models.CharField(max_length=50)
    existencias = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - {self.material}"

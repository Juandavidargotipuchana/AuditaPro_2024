from django.db import models

class Prueba(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Reporte(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    equipo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    datos = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} {self.fecha}"

class Resultado(models.Model):
    reporte = models.ForeignKey(Reporte, on_delete=models.CASCADE, null=True, blank=True)
    prueba = models.ForeignKey(Prueba, on_delete=models.CASCADE, null=True, blank=True)
    resultado = models.JSONField()

    def __str__(self):
        return f"Reporte: {self.reporte.nombre if self.reporte else ''}, Prueba: {self.prueba.nombre if self.prueba else ''}"

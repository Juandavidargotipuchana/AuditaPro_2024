from django.contrib import admin



# Register your models here.

from .models import  Resultado, Reporte, Prueba


admin.site.register(Resultado)
admin.site.register(Prueba)
admin.site.register(Reporte)


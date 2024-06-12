from django.urls import path
from . import views

urlpatterns = [
    # Vista para listar todos los reportes, utilizando un nombre descriptivo
    path('resultados/', views.ver_reportes, name='lista_resultados'),

    # Vista principal para ver reportes, misma vista que 'resultados/' pero con una ruta diferente
    path('reportes/', views.ver_reportes, name='ver_reportes'),

    # Vista de detalle para un reporte específico, usando la clave primaria del reporte
    path('reportes/detalles/<int:pk>/', views.report_detail, name='report_detail'),

    # Vista para guardar datos, nota que esta ruta estaba duplicada con diferentes prefijos
    path('guardar_datos/', views.guardar_datos, name='guardar_datos'),  # Ruta simplificada

    # Vista para generar un PDF a partir de un reporte
    path('reportes/generate_pdf/', views.generate_pdf, name='generate_pdf'),

    # Vista para listar reportes entre dos fechas especificadas
    path('reportes/entre_fechas/', views.lista_reportes, name='lista_reportes'),
    
    
    ]   



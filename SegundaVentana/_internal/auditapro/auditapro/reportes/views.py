from datetime import date
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import pdfkit

from .models import Reporte

# Vista para ver todos los reportes
def ver_reportes(request):
    reportes = Reporte.objects.all()
    return render(request, 'lista_reportes.html', {'reportes': reportes})

# Vista para listar reportes entre fechas especificadas
def lista_reportes(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    try:
        start_date = date.fromisoformat(start_date) if start_date else None
        end_date = date.fromisoformat(end_date) if end_date else None
    except ValueError:
        start_date = None
        end_date = None

    reportes = Reporte.objects.all()
    if start_date and end_date:
        reportes = reportes.filter(fecha__gte=start_date, fecha__lte=end_date)
    elif start_date:
        reportes = reportes.filter(fecha__gte=start_date)
    elif end_date:
        reportes = reportes.filter(fecha__lte=end_date)

    return render(request, 'lista_reportes.html', {'reportes': reportes})

# Detalle de un reporte específico
def report_detail(request, pk):
    reporte = get_object_or_404(Reporte, pk=pk)
    return render(request, 'report_detail.html', {'reporte': reporte})  # Corregido para enviar la clave correcta

# Guardar datos (manejando varios enfoques con CSRF y métodos HTTP)
@csrf_exempt
@require_http_methods(["POST"])
def guardar_datos(request):
    data = json.loads(request.body.decode('utf-8')) if request.body else {}
    nombre = data.get('nombre')
    equipo = data.get('equipo')
    fecha = data.get('fecha')
    datos = data.get('datos')  # Asegúrate de que esto coincide con lo que esperas en el cliente

    if not all([nombre, equipo, fecha, datos]):
        missing = [field for field in ["nombre", "equipo", "fecha", "datos"] if not data.get(field)]
        return JsonResponse({"error": f"Datos insuficientes para la creación del reporte, faltan: {', '.join(missing)}"}, status=400)

    Reporte.objects.create(nombre=nombre, equipo=equipo, fecha=fecha, datos=datos)
    return JsonResponse({"message": "Datos guardados con éxito"})

# Generar PDF desde URL
def generate_pdf(request):
    url = request.GET.get('url', '')
    if not url:
        return HttpResponse('URL parameter is missing or empty.')

    pdf = pdfkit.from_url('http://127.0.0.1:8000' + url, False)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="webpage.pdf"'
    return response


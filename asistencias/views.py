from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import IngenieríaDeSoftware, TallerDeDiseño
from django.db.models import Sum

# Diccionario para manejar asignaturas y sus modelos
ASIGNATURAS_MODELOS = {
    'ingenieria': IngenieríaDeSoftware,
    'taller': TallerDeDiseño,
}

# Landing Page
def landing_page(request):
    """Página principal accesible sin autenticación"""
    return render(request, 'landing_page.html')

# Registrar asistencia
@login_required
def registrar_asistencia(request, asignatura):
    modelo = ASIGNATURAS_MODELOS.get(asignatura)
    if not modelo:
        return redirect('landing_page')

    if request.method == 'POST':
        horas = request.POST.get('horas')
        fecha = request.POST.get('fecha')
        alumno = request.user

        # Crear el registro para la asignatura correspondiente
        modelo.objects.create(
            horas_asistidas=horas,
            alumno=alumno,
            fecha_clase=fecha
        )
        return redirect('listar_asistencias', asignatura=asignatura)

    return render(request, 'registrar_asistencia.html', {'asignatura': asignatura.title()})

# Listar asistencias
@login_required
def listar_asistencias(request, asignatura):
    modelo = ASIGNATURAS_MODELOS.get(asignatura)
    if not modelo:
        return redirect('landing_page')

    registros = modelo.objects.filter(alumno=request.user)
    suma_horas = registros.aggregate(total_horas_asistidas=Sum('horas_asistidas'))['total_horas_asistidas'] or 0

    return render(request, 'listar_asistencias.html', {
        'registros': registros,
        'asignatura': asignatura.title(),
        'suma_horas': suma_horas
    })

# Actualizar asistencia
@login_required
def actualizar_asistencia(request, asignatura, id):
    modelo = ASIGNATURAS_MODELOS.get(asignatura)
    if not modelo:
        return redirect('landing_page')

    registro = get_object_or_404(modelo, id=id)

    if request.method == 'POST':
        registro.horas_asistidas = request.POST.get('horas')
        registro.fecha_clase = request.POST.get('fecha')
        registro.save()
        return redirect('listar_asistencias', asignatura=asignatura)

    return render(request, 'actualizar_asistencia.html', {'registro': registro, 'asignatura': asignatura.title()})

# Eliminar asistencia
@login_required
def eliminar_asistencia(request, asignatura, id):
    modelo = ASIGNATURAS_MODELOS.get(asignatura)
    if not modelo:
        return redirect('landing_page')

    registro = get_object_or_404(modelo, id=id)
    registro.delete()
    return redirect('listar_asistencias', asignatura=asignatura)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('registrar/<str:asignatura>/', views.registrar_asistencia, name='registrar_asistencia'),
    path('listar/<str:asignatura>/', views.listar_asistencias, name='listar_asistencias'),
    path('actualizar/<str:asignatura>/<int:id>/', views.actualizar_asistencia, name='actualizar_asistencia'),
    path('eliminar/<str:asignatura>/<int:id>/', views.eliminar_asistencia, name='eliminar_asistencia'),
]

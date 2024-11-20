from django.db import models
from django.contrib.auth.models import User

# Modelo para Ingeniería de Software
class IngenieríaDeSoftware(models.Model):
    nombre_asignatura = models.CharField(max_length=100, default="Ingeniería de Software")
    horas_asistidas = models.PositiveIntegerField()
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_clase = models.DateField()

    def __str__(self):
        return f"{self.nombre_asignatura} - {self.alumno.username} - {self.horas_asistidas} horas - {self.fecha_clase}"


# Modelo para Taller de Diseño
class TallerDeDiseño(models.Model):
    nombre_asignatura = models.CharField(max_length=100, default="Taller de Diseño")
    horas_asistidas = models.PositiveIntegerField()
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_clase = models.DateField()

    def __str__(self):
        return f"{self.nombre_asignatura} - {self.alumno.username} - {self.horas_asistidas} horas - {self.fecha_clase}"

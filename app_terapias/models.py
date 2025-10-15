from django.db import models

class Terapia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.PositiveIntegerField(help_text="Duración en minutos")
    cita = models.DateTimeField()

    def __str__(self):
        return f'Terapia: {self.nombre}'


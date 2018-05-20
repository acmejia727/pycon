from django.db import models

# Create your models here.

class Pregunta(models.Model):
    pregunta_texto = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField('date published')

    def __str__(self):
        return (self.pregunta_texto)

class Seleccion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_seleccion = models.CharField(max_length=200)
    voto = models.IntegerField(default=0)

    def __str__(self):
        return (self.texto_seleccion)



from django.contrib import admin
from .models import Pregunta, Seleccion
# Register your models here.

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('pregunta_texto','fecha_publicacion')
    list_filter = ('pregunta_texto','fecha_publicacion')

class SeleccionAdmin(admin.ModelAdmin):
    list_display = ('pregunta','texto_seleccion','voto')
    list_filter = ('pregunta','texto_seleccion','voto')

admin.site.register(Pregunta,PreguntaAdmin)
admin.site.register(Seleccion,SeleccionAdmin)
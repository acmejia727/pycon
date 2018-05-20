from .models import *
from django.forms import ModelForm

class PreguntaForm(ModelForm):
    class Meta:
        model = Pregunta
        fields = ('__all__')
from rest_framework import serializers
from .models import *

class PreguntaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pregunta
        fields = ('__all__')
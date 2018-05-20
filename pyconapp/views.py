from django.shortcuts import render
from .models import Pregunta, Seleccion
from .forms import *
from .serializers import *
from rest_framework import viewsets

# Create your views here.

def index(request):
    pregunta = Pregunta.objects.all()

    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = PreguntaForm()

    context={
        'pregunta':pregunta,
        'form':form,
    }
    return render(request, 'index.html',context)

class Pregunta_ViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
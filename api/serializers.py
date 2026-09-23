from rest_framework import serializers
from .models import Estudiante, Tarea

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'curso', 'fechaEntrega', 'estado', 'estudiante']
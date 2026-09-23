from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tarea, Estudiante
from .serializers import TareaSerializer, EstudianteSerializer

@api_view(['GET'])
def listar_tareas(request):
    estado = request.query_params.get('estado', None)
    if estado:
        if estado not in ['pendiente', 'completada']:
            return Response({"error": "Estado inválido"}, status=status.HTTP_400_BAD_REQUEST)
        tareas = Tarea.objects.filter(estado=estado)
    else:
        tareas = Tarea.objects.all()
    serializer = TareaSerializer(tareas, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PATCH', 'DELETE'])
def detalle_tarea(request, pk):
    try:
        tarea = Tarea.objects.get(pk=pk)
    except Tarea.DoesNotExist:
        return Response({"error": "Tarea no encontrada"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TareaSerializer(tarea)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PATCH':
        serializer = TareaSerializer(tarea, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tarea.delete()
        return Response({"mensaje": "Tarea eliminada correctamente"}, status=status.HTTP_200_OK)

@api_view(['GET', 'DELETE'])
def detalle_estudiante(request, pk):
    try:
        estudiante = Estudiante.objects.get(pk=pk)
    except Estudiante.DoesNotExist:
        return Response({"error": "Estudiante no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EstudianteSerializer(estudiante)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        estudiante.delete()
        return Response({"mensaje": "Estudiante eliminado correctamente"}, status=status.HTTP_200_OK)
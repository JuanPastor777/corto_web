from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tareas/', views.listar_tareas),
    path('api/tareas/<int:pk>/', views.detalle_tarea),
    path('api/estudiantes/<int:pk>/', views.detalle_estudiante),
]
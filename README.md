# corto_web
# corto_web - API REST con Django

Proyecto de API REST desarrollado en Django para la gestión y seguimiento de tareas y estudiantes.

## Tabla de Endpoints

| Acción | Método HTTP | Endpoint |
| :--- | :--- | :--- |
| **Consultar tareas** | `GET` | `/api/tareas/` |
| **Consultar una tarea** | `GET` | `/api/tareas/{id}/` |
| **Filtrar por estado** | `GET` | `/api/tareas/?estado=pendiente` |
| **Completar tarea** | `PATCH` | `/api/tareas/{id}/` |
| **Consultar estudiante** | `GET` | `/api/estudiantes/{id}/` |
| **Eliminar estudiante** | `DELETE` | `/api/estudiantes/{id}/` |
| **Eliminar tarea** | `DELETE` | `/api/tareas/{id}/` |

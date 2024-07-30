# Django REST API for Todo Application

## Descripción

Esta es una API RESTful construida con Django y Django REST Framework para gestionar tareas (todos). La API permite crear, leer, actualizar y eliminar tareas.

## Características

- Crear, leer, actualizar y eliminar tareas.
- Filtrado, búsqueda y ordenación de tareas.
- Autenticación de usuarios (comentada en el modelo).

## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto localmente.

### Prerrequisitos

- Python 3.x
- pip
- virtualenv (opcional pero recomendado)

### Pasos

1. Clona el repositorio:
   ```sh
   git clone https://github.com/tu_usuario/Api-django-todoapp.git
   cd Api-django-todoapp
   ```
Crea y activa un entorno virtual:
  ```sh
   python venv venv
   env\Scripts\activate
  ```
Instala las dependencias:
  ```sh
   pip install -r requirements.txt
  ```
Realiza las migraciones de la base de datos:
  ```sh
   python manage.py migrate
  ```
Ejecuta el servidor de desarrollo:
  ```sh
   python manage.py runserver
  ```

Uso
Endpoints

Listar todas las tareas
  ```sh
   GET /api/todos/
  ```
Crear una nueva tarea
   ```sh
   POST /api/todos/
  ```
Obtener una tarea específica
 ```sh
   GET /api/todos/{id}/
  ```
Actualizar una tarea
  ```sh
   PUT /api/todos/{id}/
  ```
Eliminar una tarea
  ```sh
   DELETE /api/todos/{id}/
  ```

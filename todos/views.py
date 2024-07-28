from django.shortcuts import render
from .models import Todo
from rest_framework import viewsets, permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TodoSerializer
from .filters import TodoFilter

class TodoViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Todo objects """
    queryset = Todo.objects.all()  # que objetos se pueden consultar = todos
    permission_classes = [permissions.AllowAny]  # quien puede consultar = cualquiera
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = TodoFilter  # usa el filtro personalizado
    search_fields = ['title', 'description']  # reemplaza con los campos que deseas buscar
    ordering_fields = ['created']  # agrega 'created' a los campos que deseas ordenar
    
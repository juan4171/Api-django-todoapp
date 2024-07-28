from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__' #= ['id', 'title', 'description', 'created', 'datecompleted', 'user']
        read_only_fields = ('created',) #esto es para que el campo created no se pueda modificar
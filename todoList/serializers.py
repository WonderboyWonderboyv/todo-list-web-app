from rest_framework import serializers
from .models import ToDoItem
class ToDoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ToDoItem
		fields =(
			'id',
			'text',
			'done',
			)
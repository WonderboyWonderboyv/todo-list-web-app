from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import ToDoItem
from .serializers import ToDoSerializer

# Create your views here.
def home(request):
	context = locals()
	return render(request,'index.html', context)

class ToDoView(APIView):
	def get(self, request):
		todos = ToDoItem.objects.all()
		serializer = ToDoSerializer(todos, many=True)
		return Response(serializer.data)
	def put(self, request):
		serializer = ToDoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
class ToDoDetailView(APIView):
	def get(self, request, pk):
		todo = get_object_or_404(ToDoItem, pk=pk)
		serializer = ToDoSerializer(todo)
		return Response(serializer.data)
	def delete(self, request, pk):
		todo = get_object_or_404(ToDoItem, pk=pk)
		todo.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
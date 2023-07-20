from django.shortcuts import render, redirect
from django.utils.text import slugify
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import generics

# Create your views here.


def home(request):
    context = {}
    return render(request, "base/index.html", context)


class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        todo = serializer.validated_data.get('todo')
        serializer.save(todo=todo)


class TodoUpdateView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'slug'

    def perform_update(self, serializer):
        todo = serializer.validated_data.get('todo')
        slug = slugify(serializer.validated_data.get('todo'))
        instance = serializer.save(todo=todo, slug=slug)



class TodoDeleteView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'slug'


delete_view = TodoDeleteView.as_view()
update_view = TodoUpdateView.as_view()
create_list_view = TodoListCreateView.as_view()

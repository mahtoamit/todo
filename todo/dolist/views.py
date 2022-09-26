from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
# Create your views here.


#CREATE

class TodoCreate(generics.CreateAPIView):
    queryset = TooDoo.objects.all()
    serializer_class = TooDooSerializer

#READ

class TodoList(generics.ListAPIView):
    queryset = TooDoo.objects.all()
    serializer_class = TooDooSerializer

#UPDATE

class TodoDetails(generics.RetrieveUpdateAPIView):
    queryset = TooDoo.objects.all()
    serializer_class = TooDooSerializer


#DELETE

class TodoDelete(generics.DestroyAPIView):
    queryset = TooDoo.objects.all()
    serializer_class = TooDooSerializer
        




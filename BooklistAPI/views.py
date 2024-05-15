from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import  api_view

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all
    serializer_class = BookSerializer

class SingleBookView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Create your views here.



# @api_view()
# def books(request):
#     return Response('List of the books', status=status.HTTP_200_OK)
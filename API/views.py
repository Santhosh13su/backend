from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Products
from .serializer import ProductSerializer
# Create your views here.



class ProductListCreate(ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateRetriverList(RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer



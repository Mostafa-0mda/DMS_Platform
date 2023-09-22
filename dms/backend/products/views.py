#from django.shortcuts import render
from rest_framework import generics
from .models import product
from .serializers import ProductSerializer


# Create your views here.

class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = product.objects.all()
  serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()


  
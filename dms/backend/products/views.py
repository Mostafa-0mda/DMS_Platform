#from django.shortcuts import render
from pstats import Stats
import statistics
from rest_framework import generics
from .models import product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# Create your views here.

class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset = product.objects.all()
  serializer_class = ProductSerializer

  def perform_create(self, serializer):
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content') or None
    if content is None:
      content = title
    serializer.save (content=content)

product_list_create_view = ProductListCreateAPIView.as_view()




class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = product.objects.all()
  serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()




class ProductUpdateAPIView(generics.UpdateAPIView):
  queryset = product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def perform_update(self, serializer):
    instance = serializer.save()
    if not instance.content:
      instance.content = instance.title
    

product_updata_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
  queryset = product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def perform_destroy(self, instsnce):
    #instance = serializer.save()
    super().perform_destroy(instsnce)
    

product_delete_view = ProductDestroyAPIView.as_view()




# Import your Product model and ProductSerializer if they're not already imported

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            # Detail view
            obj = get_object_or_404(product, pk=pk)
            data = ProductSerializer(obj).data
            return Response(data)
        # List view
        queryset = product.objects.all().order_by("?").first()
        data = ProductSerializer(queryset).data
        return Response(data)

    if method == "POST":
        # Create Item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)

        # Handle the case where the request is invalid
        return Response(serializer.errors, status=Stats.HTTP_400_BAD_REQUEST)
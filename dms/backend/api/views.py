import statistics
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from products.models import product
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer



# Create your views here.
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    instance = product.objects.all().order_by("?").first()
    if instance:
        data = ProductSerializer(instance).data
        return Response(data)
    else:
        # Handle the case where no valid instance is found (optional).
        return Response({"message": "No products found"}, status=statistics.HTTP_404_NOT_FOUND)
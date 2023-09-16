from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from products.models import product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import productSerializer



# Create your views here.
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    instance = product.objects.all().order_by("?").first()
    data = {}
    if instance:
        #data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
        data = productSerializer(instance).data
    return Response(data)

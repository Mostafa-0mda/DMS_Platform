from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import product
from django.forms.models import model_to_dict

# Create your views here.
def api_home(request, *args, **kwargs):
  model_data = product.objects.all().order_by("?").first()
  data = {}
  if model_data:
    data['id'] = model_data.id
    data['title'] = model_data.title
    data['content'] = model_data.content
    data['price'] = model_data.price
  return JsonResponse(data)
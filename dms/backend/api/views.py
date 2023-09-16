from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def api_home(request, *args, **kwargs):
  return JsonResponse({
    "massage": "Hi there, this is your Django Api reponse !! "
  })
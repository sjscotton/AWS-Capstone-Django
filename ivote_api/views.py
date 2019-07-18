from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def index(request):
    data = {
      'Hello': 'Friend'
    }

    return JsonResponse({"data": data})
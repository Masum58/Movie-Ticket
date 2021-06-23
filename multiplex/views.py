from django.shortcuts import render
from django.http import JsonResponse, response

# Create your views here.

def multiplexHome(request):
    response ={
        "message": "multiplex home"
    }
    return JsonResponse(response)

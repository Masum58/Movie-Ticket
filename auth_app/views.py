from django.shortcuts import render
from django.http import JsonResponse, response

# Create your views here.

def authHome(request):
    response ={
        "message": "auth home"
    }
    return JsonResponse(response)

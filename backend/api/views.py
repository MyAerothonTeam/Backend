from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    prediction = {
        'dead': 12,
        'recovered': 2000,
        'newcases': 100
    }

    return JsonResponse(prediction)

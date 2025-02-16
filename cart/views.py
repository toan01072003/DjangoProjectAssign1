from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def cart_list(request):
    return HttpResponse("cart list page")
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def customer_list(request):
    return HttpResponse("Customer list page")
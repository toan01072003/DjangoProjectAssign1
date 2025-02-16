from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def book_list(request):
    return HttpResponse("book list page")
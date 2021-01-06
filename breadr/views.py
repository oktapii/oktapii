from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'breadr/index.html')

def err404(request, exception=None):
    return HttpResponseNotFound('404.html')
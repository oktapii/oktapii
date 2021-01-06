from django.http import HttpResponseNotFound
from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'breadr/index.html', {
        'year': datetime.strftime(datetime.now(), '%Y')
    })

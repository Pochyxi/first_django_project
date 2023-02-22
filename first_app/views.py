from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {
        'name': 'Adiener',
        'age': 28,
        'nationality': 'Cuban',
    }
    return render(request, 'index.html', context)

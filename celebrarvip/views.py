from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def celebrar_home(request):
    return render(request, 'celebrar/celebrar_home.html',)

# Create your views here.

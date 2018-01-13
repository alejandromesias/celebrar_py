from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    text = {'inserted_text': "hola texto insertadoss"}
    return render(request, 'nicoyvaleapp/index.html', context = text)

def intro(request):
    return render(request, 'celebrar/celebrar_home.html',)

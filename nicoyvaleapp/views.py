from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'nicoyvaleapp/nyv_home.html')

def index(request):
    text = {'inserted_text': "hola texto insertadoss"}
    return render(request, 'nicoyvaleapp/index.html', context = text)

def modelo(request):
    return render(request, 'nicoyvaleapp/modelo.html')

def intro(request):
    return render(request, 'celebrar/celebrar_home.html',)

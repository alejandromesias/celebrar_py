from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    marquesina = "3 de marzo de 2018"
    historia_parr1 = "Hay veces en la vida donde las cosas buenas llegan sin avisar y cuando menos lo esperas. Nos pasó a nosotros. Nos conocimos hace casi 9 años, pero en ese tiempo cada uno tenía un rumbo diferente... "
    historia_parr2 = "Aunque en ese momento el destino nos separó, 4 años más tarde nuestras vidas eran distintas y al encontrarnos nuevamente comenzó ésta historia. Desde ahí hemos caminado juntos, viviendo momentos únicos, aceptando quienes somos y apoyándonos en cada decisión."
    historia_parr3 = "Hace 7 meses decidimos juntar nuestras vidas para siempre y nos embarcamos en esta nueva aventura, con más retos y objetivos comunes. Estamos felices de poder compartir el inicio de ésta etapa junto a quienes más queremos."

    context_dic = {'marquesina': "testing",
                'historia_parr1': historia_parr1,
                'historia_parr2': historia_parr2,
                'historia_parr3': historia_parr3,}
    return render(request, 'nicoyvaleapp/nyv_home.html', context = context_dic)

def index(request):
    text = {'inserted_text': "hola texto insertadoss"}
    return render(request, 'nicoyvaleapp/index.html', context = text)

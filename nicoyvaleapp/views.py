from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    marquesina = "3 de marzo de 2018"
    historia_parr1 = "Hay veces en la vida donde las cosas buenas llegan sin avisar y cuando menos lo esperas. Nos pasó a nosotros. Nos conocimos hace casi 9 años, pero en ese tiempo cada uno tenía un rumbo diferente... "
    historia_parr2 = "Aunque en ese momento el destino nos separó, 4 años más tarde nuestras vidas eran distintas y al encontrarnos nuevamente comenzó esta historia. Desde ahí hemos caminado juntos, viviendo momentos únicos, aceptando quienes somos y apoyándonos en cada decisión."
    historia_parr3 = "Hace 7 meses decidimos juntar nuestras vidas para siempre y nos embarcamos en esta nueva aventura, con más retos y objetivos comunes. Estamos felices de poder compartir el inicio de ésta etapa junto a quienes más queremos."

    nombre_ceremonia = "Parroquia La Sagrada Familia del Condado"
    direccion_ceremonia = 'Gonzalo Cordero S/N y Ricardo Descalzi, Urb. "El Condado", Quito'
    hora_ceremonia = "Sábado 3  de marzo, 11h30"

    nombre_recepcion = "Hacienda Villa Vieja"
    direccion_recepcion = "Juan Procel y José Miguel Carrión, sector El Condado"
    hora_recepcion = "3 de marzo, a partir de las 13h00"
    web_recepcion = "http://haciendavillavieja.com"

    context_dic = {'marquesina': marquesina,
                'historia_parr1': historia_parr1,
                'historia_parr2': historia_parr2,
                'historia_parr3': historia_parr3,
                'nombre_ceremonia':nombre_ceremonia,
                'direccion_ceremonia':direccion_ceremonia,
                'hora_ceremonia':hora_ceremonia,
                'nombre_recepcion':nombre_recepcion,
                'direccion_recepcion':direccion_recepcion,
                'hora_recepcion':hora_recepcion,
                'web_recepcion':web_recepcion,
                }
    return render(request, 'nicoyvaleapp/nyv_home.html', context = context_dic)

def confirmar_page(request):

    marquesina = "Confirmación de Asistencia"
    instrucciones1 = "Por favor llena el siguiente formulario para confirmar tu asistencia de forma rápida y directa. "
    instrucciones2 = "Alternativamente si deseas puedes escribir un e-mail con tu confirmación a la dirección"
    email = "nickovivar@gmail.com"
    agradecimiento = "Nicolás y Valeria agradecen tu gentileza."
    context = {'marquesina': marquesina,
                'instrucciones1':instrucciones1,
                'instrucciones2':instrucciones2,
                'email': email,
                'agradecimiento' : agradecimiento,
                }

    return render(request, 'nicoyvaleapp/confirmar_page.html', context = context)

def index(request):

    text = {'inserted_text': "hola texto insertadoss"}
    return render(request, 'nicoyvaleapp/index.html', context = text)

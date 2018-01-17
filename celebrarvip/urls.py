from django.conf.urls import url
from celebrarvip import views

urlpatterns = [
    url(r'^$', views.celebrar_home, name ='home'),
]

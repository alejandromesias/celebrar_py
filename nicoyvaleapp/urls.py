from django.conf.urls import url
from nicoyvaleapp import views

urlpatterns = [
    url(r'^$', views.home, name ='home'),
    url(r'^index', views.index, name ='index'),
]

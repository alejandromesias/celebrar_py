from django.conf.urls import url
from nicoyvaleapp import views

urlpatterns = [
    url(r'^$', views.index, name ='index'),
]

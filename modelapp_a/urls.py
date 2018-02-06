from django.conf.urls import url
from modelapp_a import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name ='home'),
    url(r'^confirmar_asistencia', views.ConfirmarView.as_view(), name ='confirmar'),
]

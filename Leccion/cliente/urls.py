from django.conf.urls import include, url

from cliente.views import create, index, eliminarTicket,editarTicket
app_name = 'factura'

urlpatterns = [
    url(r'^$', index_ticket, name = 'index'),
    url(r'^createRecibo$',createRecibo, name = 'createRecibo'),
    url(r'^create$', create, name = 'create'),
    url(r'^editar/(?P<id>\d+)$', editarTicket, name='editarTicket'),
    url(r'^eliminar/(?P<id>\d+)$', eliminarTicket, name='eliminarTicket'),

    
]

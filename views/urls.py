from django.conf.urls import url
from .controller import user

urlpatterns = [

#urls para módulo de autentificación
    url(r'^$',                                                                  user.welcome,        name='login'),
    url(r'^welcome/$',      		                                            user.welcome,      name='welcome'),
    url(r'^about/$',                                                            user.about,      name='about'),
    url(r'^contact/$',                                                          user.contact,      name='contact'),
    url(r'^rooms/$',                                                            user.rooms,      name='rooms'),
    url(r'^services/$',                                                         user.services,      name='services'),


]
from django.urls import path
from . import views as core_views

urlpatterns = [
    path('', core_views.Inicio, name="home"),
    path('contacto/', core_views.contacto, name="contacto"),
]


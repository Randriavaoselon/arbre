from django.urls import path
from . import views

urlpatterns = [
    path('ajout_enfant', views.ajout_enfant, name='ajout_enfant'),
    path('liste_enfant', views.list_enfant, name='liste_enfant'),
    path('supprime/<str:id>', views.supprime, name='supprime'),
]
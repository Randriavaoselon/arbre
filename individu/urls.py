from django.urls import path
from . import views

#app_name = 'individu'

urlpatterns = [
    path('', views.page_acceuil, name='test_acceuil'),
    path('acceuil_page', views.principale, name='acceuil'),
    path('ajoute', views.enregistrer, name='ajout'),
    path('modification/<str:pk>', views.modifie, name='update'),
    path('suppression/<str:id>', views.supprime, name='delete'),
    path('sans_doulons/', views.check_id, name='identifiant'),
    path('mariage/', views.mariage_ind, name='mariage'),
    path('ajout_mariage/<str:pk>', views.ajout_mari, name='ajout_mariage'),
    path('test_form2', views.test_select2, name='test_form2'),
    path('affichage/<str:pk>', views.affichage, name='affiche'),


]
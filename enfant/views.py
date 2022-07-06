from django.shortcuts import render, redirect
from .models import Enfant, Individu
from django.contrib import messages

# Create your views here.

def ajout_enfant(request):
    if request.method == "POST":
        nom_enfant = request.POST.get("nom_enfant")
        nom_mere = request.POST.get("nom_mere")
        enfant = Individu.objects.get(id=nom_enfant)
        mere = Individu.objects.get(id=nom_mere)

        Enfant.objects.create(
            nom_enfant=enfant,
            nom_mere=mere
        )   

        return redirect('liste_enfant')
    else:
        return render(
           request,
           'enfant/ajout_enfant.html',
            {
                'individus': Individu.objects.raw("SELECT * FROM individus WHERE sex='Femme' AND id_ep<>0 AND CAST(SUBSTR(date_nais, 1, 4) AS integer) < 2004"),
                'enfants': Individu.objects.all()
            }
        )

def list_enfant(request):
    enfant = Enfant.objects.all()
    context = {'enfant': enfant}
    return render(request, 'enfant/liste_enfant.html', context)

def supprime(request, id):
    enfant = Enfant.objects.get(id=id)
    if request.method == "POST":
        enfant.delete()
        messages.error(request, 'Un enfant et une mère a été supprimer avec success!')
        return redirect("liste_enfant")
    context = {'enfant': enfant}
    return render(request, 'enfant/suppre_enfant.html', context)

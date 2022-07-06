from django.contrib import messages
from django.db.models import Q, F, Avg
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.db import connection
from django.db import transaction
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from individu.models import Individu

@login_required
def principale(request):
    individu = Individu.objects.all()

    context = {'individus': individu}
    return render(request, 'individu/acceuil.html', context)



@login_required
def enregistrer(request):
    if request.method == "POST":
        id = request.POST.get("id")
        id_ep = request.POST.get("id_ep")
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        date_nais = request.POST.get("date_nais")
        lieu = request.POST.get("lieu")
        sex = request.POST.get("sex")
        donne = Individu(id=id, id_ep=id_ep, nom=nom, prenom=prenom, date_nais=date_nais, lieu=lieu, sex=sex)
        donne.save()
        messages.success(request, 'Un individu a été ajouter avec success')
        return redirect('acceuil')
    return render(request, 'individu/ajouteForme.html')

@login_required
def modifie(request, pk=None):
    indi = Individu.objects.filter(id=pk).first()
    if request.method == "POST":
        indi.nom = request.POST["nom"]
        indi.prenom = request.POST["prenom"]
        indi.date_nais = request.POST["date_nais"]
        indi.lieu = request.POST["lieu"]
        indi.sex = request.POST["sex"]
        indi.save()
        messages.success(request, 'un individu a été modifier avec success!')
        return HttpResponseRedirect(reverse('acceuil') + '?edit_id=' + str(pk))
    context = {'indi': indi}
    template = loader.get_template('individu/modification.html')
    return HttpResponse(template.render(context, request))

@login_required
def supprime(request, id):
    individu = Individu.objects.get(id=id)
    if request.method == "POST":
        individu.delete()
        messages.error(request, 'Un individu a été supprimer avec success!')
        return redirect("acceuil")
    context = {'individu': individu}
    return render(request, 'individu/suppression.html', context)

@login_required
def check_id(request):
    if request.method == "GET":
        un = request.GET["ident"]
        check = Individu.objects.filter(id=un)
        if len(check) == 1:
            return HttpResponse("Existe")
        else:
            return HttpResponse("N' existe pas")

@login_required
def mariage_ind(request):
    H = Individu.objects.raw("SELECT * FROM individus WHERE sex='Homme' AND id_ep is NULL AND CAST(SUBSTR(date_nais, 1, 4) AS integer) <= 2004")
    F = Individu.objects.raw("SELECT * FROM individus WHERE sex='Femme' AND id_ep is NULL AND CAST(SUBSTR(date_nais, 1, 4) AS integer) <= 2004")
    context = {'femme': F, 'homme': H}
    if request.method == "POST":
        if request.POST.get('id_ep'):
            x = request.POST.get('id')
            z = request.POST.get('id_ep')
            femme = Individu.objects.select_for_update().get(id=x)
            femme.id_ep = z
            femme.save()
            return redirect('test_form2')

    return render(request, 'mariage/mariage.html', context)

@login_required
def ajout_mari(request, pk):
    ind = Individu.objects.all(id=pk).update(id_ep=F('id_ep'))
    context = {'ind': ind}
    return render(request, 'mariage/mariage.html', context)

# def test_select(request):
#     H = Individu.objects.raw("SELECT * FROM individu_individu WHERE sex='Homme'")
#     F = Individu.objects.raw("SELECT * FROM individu_individu WHERE sex='Femme'")
#     context = {'femme': F, 'homme': H}
#     if request.method == "POST":
#         if request.POST.get('id_ep'):
#             x = request.POST.get('id')
#             z = request.POST.get('id_ep')
#             femme = Individu.objects.select_for_update().get(id=x)
#             femme.id_ep = z
#             femme.save()
#             return redirect('test_form2')
#
#     return render(request, 'teste/teste.html', context)

@login_required
def test_select2(request):
    H = Individu.objects.raw("SELECT * FROM individus WHERE sex='Homme' AND CAST(SUBSTR(date_nais, 1, 4) AS integer) <= 2004")
    F = Individu.objects.raw("SELECT * FROM individus WHERE sex='Femme' AND CAST(SUBSTR(date_nais, 1, 4) AS integer) <= 2004")
    context = {'femme': F, 'homme': H}
    if request.method == "POST":
        if request.POST.get('id_ep'):
            x = request.POST.get('id')
            z = request.POST.get('id_ep')
            femme = Individu.objects.select_for_update().get(id=x)
            femme.id_ep = z
            femme.save()
            return redirect('acceuil')

    return render(request, 'mariage/teste2.html', context)


@login_required
def affichage(request, pk):
    affichage_ind = Individu.objects.get(id=pk)
    context = {'affichage': affichage_ind}
    return render(request, 'individu/affichage.html', context)


def page_acceuil(request):

    return render(request, 'Acceuil/acceuil_page.html')

from urllib import request

from django.shortcuts import render,redirect,get_object_or_404
from .models import AchatDevises
from .form import CustomUserCreationForm,AchatDevisesForm
from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form= CustomUserCreationForm()
        return render(request,'inscription.html',{'form':form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('acceuil')
        else:
            messages.error(request,'Nom d\'utilisateur ou mot de pass incorrect')
    return render(request,'connexion.html')
@login_required
def acceuil(request):
    return render(request,'acceuil.html')
@login_required
def achat(request):
    return render(request ,'achat.html')
@login_required
def vente(request):
    return render(request,'vente.html')
@login_required
def deconnexion(request):
    logout(request)
    return redirect('connexion')

@login_required
def achat_devise(request, id=None):
    if id:
        achat = get_object_or_404(AchatDevises, id=id)
    else:
        achat = None

    if request.method == "POST":
        form = AchatDevisesForm(request.POST, instance=achat)

        if form.is_valid():
            form.save()
            return redirect("achat")
    else:
        form = AchatDevisesForm(instance=achat)

    achats = AchatDevises.objects.all()

    context = {
        "form": form,
        "achats": achats,
        "achat": achat,
    }

    return render(request, "achat.html", context)

def supprimer(request, id):
    achat = get_object_or_404(AchatDevises, id=id)
    achat.delete()

    return redirect("achat")
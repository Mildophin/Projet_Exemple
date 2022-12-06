from django.shortcuts import render, redirect
from Base.models import *
from Base.forms import *


def create(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        name = request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        form = CreateForm(request.POST)
        if form.is_valid():
            Personne.objects.create_personne(first_name=first_name, name=name, date_of_birth=date_of_birth)
            return redirect("create")


def display(request):
    personne_objects = Personne.objects.all().order_by("name", "first_name")
    return render(request, "display.html", context={"personnes_list": personne_objects})
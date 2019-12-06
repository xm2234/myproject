from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Squirrel
from .forms import SquirrelForm

def map(request):
    squirrels = Squirrel.objects.all()
    context = {
        'sightings':squirrels,
    }
    return render(request, 'sightings/map.html',context)

def sightings(request):
    sightings = Squirrel.objects.all()
    context = {
        'squirrels': sightings,
    }
    return render(request, 'sightings/sightings.html',context)

def update(request, Unique_Squirrel_ID):
    squirrel = Squirrel.objects.filter(id=Unique_Squirrel_ID)[0]
    if request.method == 'Post':
        # check form data
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{Unique_Squirrel_ID}')
    else:
        form = SquirrelForm()
    context = {
        'form': form,
    }
    return render(request, 'sightings/edit.html', context)

def add(request):
    if request.method == 'POST':
        # check form data
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/list/')
    else:
        form = SquirrelForm()
    context = {
        'form': form,
    }
    return render(request, 'sightings/edit.html', context)

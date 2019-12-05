from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Squirrel
from .forms import SquirrelForm

def all_squirrel(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels,
    }
    return render(request, 'sightings/all.html',context)

def squirrel_details(request, Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(id=Unique_Squirrel_ID)
    return HttpResponse(pet.name)
def edit_pet(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    if request.method == 'Post':
        # check form data
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect(f'/adopt/{pet_id}')
    else:
        form = PetForm()
    context = {
        'form': form,
    }
    return render(request, 'adopt/edit.html', context)

def add_squirrel(request):
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

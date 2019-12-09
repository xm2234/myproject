from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.db import connection

from .models import Squirrel
from .forms import SquirrelForm
import random



def sightings(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'sightings/sightings.html',context)

def map(request):
    squirrel_100 = random.sample(range(Squirrel.objects.all().count()),10)
    squirrels_ = [Squirrel.objects.all()[i] for i in squirrel_100]
    context = {
        'squirrels':squirrels_,
    }
    return render(request, 'sightings/map.html',context)

def update(request, Unique_Squirrel_ID):
    squirrel = Squirrel.objects.filter(Unique_Squirrel_ID = Unique_Squirrel_ID)[0]
    if request.method == 'Post':
        # check form data
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{Unique_Squirrel_ID}')
    else:
        form = SquirrelForm(instance=squirrel)
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
            return redirect(f'/sightings/')
    else:
        form = SquirrelForm()
    context = {
        'form': form,
    }
    return render(request, 'sightings/add.html', context)

def stats(request):
    
    #age
    with connection.cursor() as c:
        c.execute("select age,count(*) from sightings_Squirrel s group by age")
        result = c.fetchall()
        dict_1=dict()
        for i in range(len(result)):
            dict_1[result[i][0]] = result[i][1]
    
    #primary fur color
    with connection.cursor() as c:
        c.execute("select primary_fur_color,count(*) from sightings_Squirrel s group by primary_fur_color") 
        result = c.fetchall()
        dict_2=dict() 
        for i in range(len(result)):
            dict_2[result[i][0]] = result[i][1]
    
    #location
    with connection.cursor() as c:
        c.execute("select location,count(*) from sightings_Squirrel s group by location") 
        result = c.fetchall()
        dict_3=dict() 
        for i in range(len(result)):
            dict_3[result[i][0]] = result[i][1]
    
    #running
    with connection.cursor() as c:
        c.execute("select running,count(*) from sightings_Squirrel s group by running") 
        result = c.fetchall()
        dict_4=dict() 
        for i in range(len(result)):
            dict_4[result[i][0]] = result[i][1]
    
    #chasing
    with connection.cursor() as c:
        c.execute("select chasing,count(*) from sightings_Squirrel s group by chasing")
        result = c.fetchall()
        dict_5=dict()
        for i in range(len(result)):
            dict_5[result[i][0]] = result[i][1]
    return render(request,'sightings/stats.html',locals())

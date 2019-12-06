from django.urls import path

from . import views

urlpatterns = [    
    path('map/',views.map),
    path('sightings/',views.sightings),
    path('sightings/stats/',views.stats,name='stats'),
    path('sightings/add/',views.add,name='add'),
    path('sightings/<unique-squirrel-id>', views.update,name='update'),

]

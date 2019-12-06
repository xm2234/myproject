from django.urls import path

from . import views

urlpatterns = [
    path('map/',views.map),
    # path('/sightings/<unique-squirrel-id>', views.update),

]

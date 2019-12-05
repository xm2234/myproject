import csv

from django.core.management.base import BaseCommand

from sightings .models import Squirrel

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        for item in data:
            s = Squirrel(
                Latitude = item['Latitude'],
                Longitude = item['Longitude'],
                Unique_Squirrel_ID = item['Unique Squirrel ID'],
                Shift = item['Shift'],
                Date = item['Date'],
                Age = item['Age'],
                Primary_Fur_Color = item['Primary Fur Color'],
                Location = item['Location'],
                Specific_Location = item['Specific_Location'],
                Running = item['Running'],
                Chasing = item['Chasing'],
                Climbing = item['Climbing'],
                Eating = item['Eating'],
                Foraging = item['Foraging'],
                Other_Activities = item['Other Activities'],
                Kuks = item['Kuks'],
                Quaas = item['Quaas'],
                Moans = item['Moans'],
                Tail_flags = item['Tail flags'],
                Tail_twitches = item['Tail twitches'],
                Approaches = item['Approaches'],
                Indifferent = item['Indifferent'],
                Runs_from = item['Runs from'],
            )
            s.save()
             
import csv

from django.core.management.base import BaseCommand

from sightings .models import Squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            next(reader)
            data = list()
            for item in reader:
                if item['Unique Squirrel ID'] in data:
                    pass
                else:
                    data.append(item['Unique Squirrel ID'])
                    date = item['Date']
                    y = date[4:]
                    m = date[:2]
                    d = date[2:4]
                    formal_date = y + '-' + m + '-' + d
                    s = Squirrel(
                        Latitude = item['X'],
                        Longitude = item['Y'],
                        Unique_Squirrel_ID = item['Unique Squirrel ID'],
                        Shift = item['Shift'],
                        Date = formal_date,
                        Age = item['Age'],
                        Primary_Fur_Color = item['Primary Fur Color'],
                        Location = item['Location'],
                        Specific_Location = item['Specific Location'],
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
             

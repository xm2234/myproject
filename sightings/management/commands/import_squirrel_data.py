import csv

from django.core.management.base import BaseCommand, CommandError

from sightings .models import Squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def str_to_bool(self,x):
        if x =='true':
            return True
        else:
            return False

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
                        Running = self.str_to_bool(item['Running']),
                        Chasing = self.str_to_bool(item['Chasing']),
                        Climbing = self.str_to_bool(item['Climbing']),
                        Eating = self.str_to_bool(item['Eating']),
                        Foraging = self.str_to_bool(item['Foraging']),
                        Other_Activities = item['Other Activities'],
                        Kuks = self.str_to_bool(item['Kuks']),
                        Quaas = self.str_to_bool(item['Quaas']),
                        Moans = self.str_to_bool(item['Moans']),
                        Tail_flags = self.str_to_bool(item['Tail flags']),
                        Tail_twitches = self.str_to_bool(item['Tail twitches']),
                        Approaches = self.str_to_bool(item['Approaches']),
                        Indifferent = self.str_to_bool(item['Indifferent']),
                        Runs_from = self.str_to_bool(item['Runs from']),
                    )
                    s.save()
             

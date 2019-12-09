import csv
from django.core.management import BaseCommand
from sightings.models import Squirrel

class Command(BaseCommand):
    
    def add_arguments(self,parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file'],'w') as fp:
            writer = csv.writer(fp)
            header = ['Latitude','Longitude','Unique_Squirrel_ID',
                    'Shift','Date','Age','Primary_Fur_Color','Location',
                    'Specific_Location','Running','Chasing',
                    'Climbing','Eating','Foraging','Other_Activities',
                    'Kuks','Quaas','Moans','Tail_flags', 
                    'Tail_twitches','Approaches','Indifferent', 
                    'Runs_from']
            writer.writerow(header)

            data = Squirrel.objects.all()
            for item in data:
                writer.writerow([item.Latitude,item.Longitude,item.Unique_Squirrel_ID,
                    item.Shift,item.Date,item.Age,item.Primary_Fur_Color,item.Location,
                    item.Specific_Location,item.Running,item.Chasing,item.Climbing,
                    item.Eating,item.Foraging,item.Other_Activities,item.Kuks,
                    item.Quaas,item.Moans,item.Tail_flags,item.Tail_twitches,
                    item.Approaches,item.Indifferent,item.Runs_from])




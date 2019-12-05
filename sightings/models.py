from django.db import models

class Squirrel(models.Model):
    Latitude=models.FloatField(null=True)
    Longitude=models.FloatField(null=True)
    Unique_Squirrel_ID=models.CharField(
        max_length=18,
        null = True,
    )
    AM='AM'
    PM='PM'
    DATE_TIME_CHOICES=(
        (AM,'AM'),
        (PM,'PM'),
    )
    Shift=models.CharField(
        max_length = 18,
        choices=DATE_TIME_CHOICES,
        default=AM,
    )
    Date=models.DateField(null=True)
    Age=models.CharField(
        max_length=10,
        null = True,
    )
    Primary_Fur_Color=models.CharField(
        max_length=18,
        null = True,
    )
    Location=models.CharField(
        max_length=20,
        null = True,
    )
    Specific_Location=models.CharField(
        max_length=100,
        null = True,
    )
    Running=models.BooleanField(null=True)
    Chasing=models.BooleanField(null=True)
    Climbing=models.BooleanField(null=True)
    Eating=models.BooleanField(null=True)
    Foraging=models.BooleanField(null=True)
    Other_Activities=models.CharField(
        max_length=100,
        null = True,
    )
    Kuks=models.BooleanField(null=True)
    Quaas=models.BooleanField(null=True)
    Moans=models.BooleanField(null=True)
    Tail_flags=models.BooleanField(null=True)
    Tail_twitches=models.BooleanField(null=True)
    Approaches=models.BooleanField(null=True)
    Indifferent=models.BooleanField(null=True)
    Run_from=models.BooleanField(null=True)

    def __str__(self):
        return self.Unique_Squirrel_ID

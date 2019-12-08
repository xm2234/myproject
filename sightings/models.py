from django.db import models

class Squirrel(models.Model):
    Latitude = models.FloatField(blank=True, null=True)
    Longitude = models.FloatField(blank=True, null=True)
    Unique_Squirrel_ID = models.CharField(
        max_length = 100,
        blank=True,
        null = True,
    )
    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = (
        (AM,'AM'),
        (PM,'PM'),
    )
    Shift = models.CharField(
        max_length = 18,
        choices = SHIFT_CHOICES,
        blank=True, 
        null=True,
    )

    Date = models.DateField(blank=True, null=True)

    ADULT = 'Adult'
    JUVENILE ='Juvenile'
    OTHER ='?'
    
    AGE_CHOICES = (
            (ADULT,'Adult'),
            (JUVENILE,'Juvenile'),
            (OTHER,'Unknown'),
    )

    Age = models.CharField(
        max_length = 20,
        choices = AGE_CHOICES,
        null = True,
        blank = True,
    )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    PRIMARY_COLOR_CHOICES = (
        (GRAY,'Gray'),
        (CINNAMON,'Cinnamon'),
        (BLACK,'Black'),
    )

    Primary_Fur_Color = models.CharField(
        max_length = 18,
        choices = PRIMARY_COLOR_CHOICES,
        null = True,
        blank = True,
    )

    ABOVE_GROUND = 'Above Ground'
    GROUND_PLANE = 'Ground Plane'
    LOCATION_CHOICES = (
            (GROUND_PLANE,'Ground Plane'),
            (ABOVE_GROUND,'Above Ground'),
    )
    Location = models.CharField(
        max_length = 20,
        choices = LOCATION_CHOICES,
        null = True,
        blank=True,
    )
    Specific_Location=models.CharField(
        max_length=100,
        null = True,
        blank = True,
    )

    Running=models.BooleanField(blank=True, null=True)

    Chasing=models.BooleanField(blank=True, null=True)
    
    Climbing=models.BooleanField(blank=True, null=True)
    
    Eating=models.BooleanField(blank=True, null=True)
    
    Foraging=models.BooleanField(blank=True, null=True)
    
    Other_Activities=models.CharField(
        max_length=100,
        null = True,
        blank = True,
    )
    
    Kuks=models.BooleanField(blank=True, null=True)
    
    Quaas=models.BooleanField(blank=True, null=True)
    
    Moans=models.BooleanField(blank=True, null=True)
    
    Tail_flags=models.BooleanField(blank=True, null=True)
    
    Tail_twitches=models.BooleanField(blank=True, null=True)
    
    Approaches=models.BooleanField(blank=True, null=True)
    
    Indifferent=models.BooleanField(blank=True, null=True)
    
    Runs_from=models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.Unique_Squirrel_ID

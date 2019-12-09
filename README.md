# Squirrel Tracking Application
This is an app that can start keeping track of all the known squirrels and plans to start with Central Park. It uses 2018 Central Park Squirrel Census data and allow users to add, update, and view squirrel data. 

# Main Functions
## Management commands

There are two management commands:
1,import_squirrel_data: 
  import the data from a CSV file
2,export_squirrel_data: 
  export the data in CSV format
  
## Views
There're five views in the web app:

### map
Located at: /map
Shows a map that displays the location of the squirrel sightings on an OpenStreets map

### sightings

Located at: /sightings
Shows the list of squirrel sightings

### Update
Located at: /sightings/<Unique_Squirrel_ID>
Shows details of a particular sighting and edit the sightings of the squirrel of the unique squirrel id

### add
Located at: /sightings/add
Allows users to create new sightings
Fields supported: Fields supported: Latitude, Longitude, Unique Squirrel ID, Shift, Date, Age, Primary Fur Color, Location, Specific Location, Running, Chasing, Climbing, Eating, Foraging, Other Activities, Kuks, Quaas, Moans, Tail flags, Tail twitches, Approaches, Indifferent, Runs from

### stats
Located at: /sightings/stats
Shows general stats about the sightings

# Group Name
Project Group 61, Section 1

# UNIs
[sw3439,xm2234]


# Server Link
https://kinetic-harbor-255421.appspot.com

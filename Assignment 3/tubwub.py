#******************************************************************************
# tubwub.py
#******************************************************************************
# Name: Wengsing Wong
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# docs.python.org
# stackoverflow.com
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
# I did not attempt the challenge.

# Import the math module to access the sqrt function
import math

# Latitude and longitude of Tubwub's HQ
TUBWUB_LAT = 40.740230
TUBWUB_LONG = -73.983766

# Ask user to input latitude and longitude of event's location, the price per 
# ticket, and whether or not the event is "hot".
# Then convert the latitude, longitude, and ticket price to floats
event_lat = float(input("Please enter the event's latitude: "))
event_long = float(input("Please enter the event's longitude: "))
ticket_price = float(input("Please enter the ticket price ($): "))
event_hotness = input("Is the event hot? (y/n) ")

# Calculate the difference between the latitudes and longitudes, convert them
# to kilometers, and then calculate and display the distance between Tubwub's 
# HQ and the event
lat_diff = (TUBWUB_LAT - event_lat) * 111.048
long_diff = (TUBWUB_LONG - event_long) * 84.515
distance = math.sqrt((lat_diff ** 2) + (long_diff ** 2))
print("\nDistance:", distance)

# Compare the distance to the maximum allowable distance and factor in whether
# the event is hot to determine how many tickets to buy
if distance > 3.0 or event_hotness == 'n':
    print("\nBuy 0 tickets")
else:
    tickets_to_buy = int(150.00 // ticket_price)
    
    if tickets_to_buy == 1:
        print("\nBuy {0} ticket".format(tickets_to_buy))
    else:
        print("\nBuy {0} ticket(s)".format(tickets_to_buy))


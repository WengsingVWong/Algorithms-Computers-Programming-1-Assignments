#******************************************************************************
# escape.py
#******************************************************************************
# Name: Wengsing Wong
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# docs.python.org
# purplemath.com
# Mizan Mizan
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
# I did not attempt the challenge.

# Import the random module to access the random function
import random

# Import the math module to access the sqrt function
import math

# Initialize the (least distance) running sum and (distance) counter variables
ld_rs = 0
d_counter = 0

# Create a variable to hold the number of simulations
NUM_OF_SIM = 10 ** 5

# Store the coordinates of the 3 exits in appropriate variables
EXIT1XC = 0
EXIT1YC = 0.2
EXIT2XC = 0.2
EXIT2YC = 0
EXIT3XC = 1
EXIT3YC = 1

# Use a for loop to run the simulations
for i in range(NUM_OF_SIM):
    
    # Randomly generate the coordinates of where the person is dropped in the 
    # room
    xc = random.random()
    yc = random.random()
    
    # Calculate the distance to each of the three exits
    dist1 = math.sqrt(((EXIT1XC - xc) ** 2) + (EXIT1YC - yc) ** 2)
    dist2 = math.sqrt(((EXIT2XC - xc) ** 2) + (EXIT2YC - yc) ** 2)
    dist3 = math.sqrt(((EXIT3XC - xc) ** 2) + (EXIT3YC - yc) ** 2)
    
    # Determine which distance is the least
    if (dist1 < dist2):
        least_dist = dist1
    else:
        least_dist = dist2

    if (dist3 < least_dist):
        least_dist = dist3
    
    # Add the least distance to the running sum variable
    ld_rs += least_dist
    
    # Increment the counter variable if the shortest distance happens to be 
    # less than 0.4
    if (least_dist < 0.4):
        d_counter += 1

# Calculate the average distance and probability
avg_dist = ld_rs / 100000
prob = (d_counter / 100000) * 100

# Print the average distance and probability
print("Average Distance:", avg_dist)
print("\nProbability That the Person Has to Run Less Than 0.4: {0}%".format(prob))
#******************************************************************************
# population.py
#******************************************************************************
# Name: Wengsing Wong
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used): 
# 
# docs.python.org
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

# Import the math module in order to access the e^x function
import math

# Ask the user to input the initial population, the first time period, and the 
# first growth rate, and store them in the appropriate variables
population = input("Please enter the initial population: ")
time_period = input("Please enter the first time period (in years): ")
growth_rate = input("Please enter the first growth rate (as a percent, but without the % symbol): ")

# Convert the inputted strings to floats and convert the growth rate to a decimal
population = float(population)
time_period = float(time_period)
growth_rate = float(growth_rate) / 100.0

# Calculate the new population (1) and store it in the population variable
population = population * (math.exp(growth_rate * time_period))

# Ask the user for the second time period and growth rate and store them in the
# appropriate variables
time_period = input("Please enter the second time period (in years): ")
growth_rate = input("Please enter the second growth rate (as a percent, but without the % symbol): ")

# Convert the inputted strings to floats and convert the growth rate to a decimal
time_period = float(time_period)
growth_rate = float(growth_rate) / 100.0

# Calculate the new population (2) and store it in the population variable
population = population * (math.exp(growth_rate * time_period))

# Ask the user for the third time period and growth rate and store them in the
# appropriate variables
time_period = input("Please enter the third time period (in years): ")
growth_rate = input("Please enter the third growth rate (as a percent, but without the % symbol): ")

# Convert the inputted strings to floats and convert the growth rate to a decimal
time_period = float(time_period)
growth_rate = float(growth_rate) / 100.0

# Calculate the new population (3) and store it in the population variable
population = population * (math.exp(growth_rate * time_period))

# Print the final population
print("\nThe final population is ", population)
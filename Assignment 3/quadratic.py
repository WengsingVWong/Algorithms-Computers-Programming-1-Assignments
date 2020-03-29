#******************************************************************************
# quadratic.py
#******************************************************************************
# Name: Wengsing Wong
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# khanacademy.org
# google.com
# mathisfun.com
# geeksforgeeks.org
# stackoverflow.com
# Mizan Mizan
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
# I did not attempt the challenge.
#

# Import the math module in order to use the sqrt() function
import math

# Ask user to input coefficients and convert them to floats
avalue = float(input("Please enter the x^2 coefficient (a): "))
bvalue = float(input("Please enter the x^1 coefficient (b): "))
cvalue = float(input("Please enter the x^0 coefficient (c): "))

# Calculate discriminant
discriminant = (bvalue**2) - (4 * avalue * cvalue)

# If discriminant > 0, then there will be 2 solutions
# Calculate the roots and format them with 4 decimal places
if discriminant > 0:
    xone = ((-1 * bvalue) + math.sqrt(discriminant)) / (2 * avalue)
    xtwo = ((-1 * bvalue) - math.sqrt(discriminant)) / (2 * avalue)
    print("\nTWO REAL SOLUTIONS: x = {0:.4f} and {1:.4f}".format(xone, xtwo))
    
# If discriminant = 0, then there will be 1 solution
# Calculate the root and format it with 4 decimal places
elif discriminant == 0:
    xone = (-1 * bvalue) / (2 * avalue)
    print("\nONE REAL SOLUTION: x = {0:.4f}".format(xone))

# Otherwise, discriminant < 0, and there will be 2 complex solutions
# Calculate the complex roots and format them with 4 decimal places
else:
    xonereal = (-1 * bvalue) / (2 * avalue) 
    xoneimag = (math.sqrt(abs(discriminant))) / (2 * avalue)
    print("\nCOMPLEX SOLUTIONS: x = {0:.4f} - {1:.4f}i and x = {0:.4f} + {1:.4f}i".format(xonereal, xoneimag))
#******************************************************************************
# triangle.py
#******************************************************************************
# Name: Wengsing Wong
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#  
# docs.python.org
# mathisfun.com
# google.com
# khanacademy.org
# openbookproject.net
# stackoverflow.com
# math.stackexchange.com
# Mizan Mizan
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

# Import the math module in order to access the arcsin, arccos, and sin functions
import math

# Ask the user to input the three side lengths
largest_side = input("Please enter the largest side length: ")
middle_side = input("Please enter the middle side length: ")
smallest_side = input("Please enter the smallest side length: ")

# Convert the inputted strings to floats
largest_side = float(largest_side)
middle_side = float(middle_side)
smallest_side = float(smallest_side)

# Validate user input
if (largest_side < 0 or middle_side < 0 or smallest_side < 0):
    print("\nOne or more side lengths you entered are negative.")
    print ("\nPlease restart the program and enter three positive side lengths.")
elif (largest_side < middle_side or middle_side < smallest_side):
    print("\nThe side lengths you entered are not in descending order.")
    print("\nPlease restart the program and enter three side lengths in descending order.")
elif ((largest_side + middle_side < smallest_side) or (middle_side + smallest_side < largest_side) or (smallest_side + largest_side < middle_side)):
    print("\nThe side lengths you entered do not satisfy the triangle inequality.")
    print("\nPlease restart the program and enter three side lengths that satisfy the triangle inequality.") 
else:
    
    # Use the Law of Cosines to calculate the largest angle (in RADIANS)
    largest_angle = math.acos((largest_side**2 - smallest_side**2 - middle_side**2) / (-2 * smallest_side * middle_side))
    
    # Use the Law of Sines to calculate the middle angle (in RADIANS)
    middle_angle = math.asin(middle_side * (math.sin(largest_angle) / (largest_side)))
    
    # Calculate the smallest angle (in RADIANS)
    smallest_angle = math.pi - (largest_angle + middle_angle)
    
    # Convert the three angles to degrees
    largest_angle = largest_angle * (180 / math.pi)
    middle_angle = middle_angle * (180/ math.pi)
    smallest_angle = smallest_angle * (180/math.pi)
    
    # Print the values of the three angles
    print("\nThe three angles are: \n")
    print(largest_angle)
    print()
    print(middle_angle)
    print()
    print(smallest_angle)
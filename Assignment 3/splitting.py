#******************************************************************************
# splitting.py
#******************************************************************************
# Name: Wengsing Wong
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# google.com
# Mizan MIzan
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

# Ask the user to input the coordinates of 4 points on a plane and convert them
# to floats
x1 = float(input("Enter the x-coordinate of the 1st point: "))
y1 = float(input("Enter the y-coordinate of the 1st point: "))

x2 = float(input("Enter the x-coordinate of the 2nd point: "))
y2 = float(input("Enter the y-coordinate of the 2nd point: "))

x3 = float(input("Enter the x-coordinate of the 3rd point: "))
y3 = float(input("Enter the y-coordinate of the 3rd point: "))

x4 = float(input("Enter the x-coordinate of the 4th point: "))
y4 = float(input("Enter the y-coordinate of the 4th point: "))

# Ask the user to input values for m and b and convert them to floats
mvalue = float(input("Enter a value for m: "))
bvalue = float(input("Enter a value for b: "))

# Define the "above the line" and "below the line" counter variables
above_line_ctr = 0
below_line_ctr = 0

# For each point, calculate the corresponding y-value on the given line using 
# the given x-value and compare it to the given y-value. If the calculated
# y-value > given y-value, then increment 
if y1 > ((mvalue * x1) + bvalue):       # 1st point
    above_line_ctr = above_line_ctr + 1 # Point is above the line
elif y1 < ((mvalue * x1) + bvalue):
    below_line_ctr = below_line_ctr + 1 # Point is below the line
else:
    above_line_ctr = above_line_ctr + 1 # Point is on the line and is treated
    below_line_ctr = below_line_ctr + 1 # as being both above and below the line

if y2 > ((mvalue * x2) + bvalue):       # 2nd point
    above_line_ctr = above_line_ctr + 1 # Point is above the line
elif y2 < ((mvalue * x2) + bvalue):
    below_line_ctr = below_line_ctr + 1 # Point is below the line
else:
    above_line_ctr = above_line_ctr + 1 # Point is on the line and is treated
    below_line_ctr = below_line_ctr + 1 # as being both above and below the line

if y3 > ((mvalue * x3) + bvalue):       # 3rd point
    above_line_ctr = above_line_ctr + 1 # Point is above the line
elif y3 < ((mvalue * x3) + bvalue):
    below_line_ctr = below_line_ctr + 1 # Point is below the line
else:
    above_line_ctr = above_line_ctr + 1 # Point is on the line and is treated
    below_line_ctr = below_line_ctr + 1 # as being both above and below the line

if y4 > ((mvalue * x4) + bvalue):       # 4th point
    above_line_ctr = above_line_ctr + 1 # Point is above the line
elif y4 < ((mvalue * x4) + bvalue):
    below_line_ctr = below_line_ctr + 1 # Point is below the line
else:
    above_line_ctr = above_line_ctr + 1 # Point is on the line and is treated
    below_line_ctr = below_line_ctr + 1 # as being both above and below the line

# Check to see how many points are above the line and how many are below it
if (above_line_ctr >= 2 and below_line_ctr >= 2):
    print("\nSplitting")
else:
    print("\nNot Splitting")
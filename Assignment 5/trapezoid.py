#******************************************************************************
# trapezoid.py
#******************************************************************************
# Name: Wengsing Wong
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# docs.python.org
# brownmath.com
# Mizan Mizan
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
# I did not attempt the challenge.

# Import the math module to access the cosine trig function and pi variable
import math

# Define f(x) as given in the problem
def f_of_x(x):
    if x < 0:
        result = (1 + x) * math.cos(math.pi * x)
    else:
        result = (1 - x) * math.cos(math.pi * x)
    return result

# Ask the user to input values for N, a, and b, and convert them to the appropriate
# data type
N = int(input("Enter the number of trapezoids to be used in this approximation: "))
a = float(input("Enter the lower boundary: "))
b = float(input("Enter the upper boundary: "))

# Calculate the change in x (the height of each trapezoid)
ch_in_x = (b - a) / N

# Create a running sum variable and initialize it to 0
rs = 0

# Add up all the terms
for i in range(N + 1):
    if (i == 0) or (i == N):
        rs += (f_of_x(a + i * ch_in_x))
    else:
        rs += 2 * (f_of_x(a + i * ch_in_x))

# Multiply the running sum by ch_in_x / 2 to calculate the estimated total area
# under the curve
est_area = rs * (ch_in_x / 2)

# Print the estimated total area
print("\nApproximate Total Area Under the Curve:", est_area)
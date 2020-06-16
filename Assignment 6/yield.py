#******************************************************************************
# yield.py
#******************************************************************************
# Name: Wengsing Wong
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# mathisfun.com
# docs.python.org
# google.com
# Mizan Mizan
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
# I did not attempt the challenge.

# Import the math module
import math

# Ask the user to enter values for the following variables and convert them to
# integers
B = int(input("Enter a value for B: "))
c1 = int(input("Enter a value for c1: "))
c2 = int(input("Enter a value for c2: "))
c3 = int(input("Enter a value for c3: "))
T1 = int(input("Enter a value for T1: "))
T2 = int(input("Enter a value for T2: "))
T3 = int(input("Enter a value for T3: "))

# =============================================================================
# print("B:", B)
# print("c1:", c1, "c2:", c2, "c3:", c3)
# print("T1:", T1, "T2:", T2, "T3:", T3)
# =============================================================================

# Starting test value of x
x = 0.1

# Apply Newton's method 100 times
for approx in range(1, 101):
    f_of_x = (c1 * math.exp(-1 * x * T1)) + (c2 * math.exp(-1 * x * T2)) + (c3 * math.exp(-1 * x * T3)) - B
    f_p_of_x = (-1 * T1 * c1 * math.exp(-1 * x * T1)) - (T2 * c2 * math.exp(-1 * x * T2)) - (T3 * c3 * math.exp(-1 * x * T3))
    x -=  f_of_x / f_p_of_x

# Output the result
print("\nx100 = {0}, or {1}%".format(x, x * 100))
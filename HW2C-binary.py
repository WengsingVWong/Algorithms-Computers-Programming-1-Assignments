#******************************************************************************
# binary.py
#******************************************************************************
# Name: Wengsing Wong
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# pythoncentral.io
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

# Import the random module in order to access the random function
import random

# Generate the 8 digit binary number
bdigit1 = random.randrange(0,2)
bdigit2 = random.randrange(0,2)
bdigit3 = random.randrange(0,2)
bdigit4 = random.randrange(0,2)
bdigit5 = random.randrange(0,2)
bdigit6 = random.randrange(0,2)
bdigit7 = random.randrange(0,2)
bdigit8 = random.randrange(0,2)

# Convert the binary number to base-10
dec_num = (bdigit1 * 128) + (bdigit2 * 64) + (bdigit3 * 32) + (bdigit4 * 16) + (bdigit5 * 8) + (bdigit6 * 4) + (bdigit7 * 2) + (bdigit8 * 1)

# Print the result
print("Here's a random example of binary!")
print("The binary number", bdigit1, bdigit2, bdigit3, bdigit4, bdigit5, bdigit6, bdigit7, bdigit8, "is equivalent to the decimal number", dec_num, end = "")
print(".")

# Ask the user to input a decimal number between 0 and 255
dec_num = input("Now, please enter a decimal number between 0 and 255 (integers only): ")

# Convert the inputted string to an integer
dec_num = int(dec_num)

# Convert the decimal number to binary
bdigit1 = dec_num // 128
dec_num = dec_num - (bdigit1 * 128)
bdigit2 = dec_num // 64
dec_num = dec_num - (bdigit2 * 64)
bdigit3 = dec_num // 32
dec_num = dec_num - (bdigit3 * 32)
bdigit4 = dec_num // 16
dec_num = dec_num - (bdigit4 * 16)
bdigit5 = dec_num // 8
dec_num = dec_num - (bdigit5 * 8)
bdigit6 = dec_num // 4
dec_num = dec_num - (bdigit6 * 4)
bdigit7 = dec_num // 2
dec_num = dec_num - (bdigit7 * 2)
bdigit8 = dec_num

# Print the result
print("That number is equivalent to the binary number", bdigit1, bdigit2, bdigit3, bdigit4, bdigit5, bdigit6, bdigit7, bdigit8, end = "")
print(".")
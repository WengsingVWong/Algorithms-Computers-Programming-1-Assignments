#******************************************************************************
# bricks.py
#******************************************************************************
# Name: Wengsing Wong
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# NONE
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
# I did not attempt the challenge.

# Import the turtle module
import turtle

# Ask the user to input values for x and y and convert them to integers
x = int(input("Enter a positive integer for x: "))
y = int(input("Enter a positive integer for y: "))

# Create the screen and main turtle
tscr = turtle.Screen()
koopa = turtle.Turtle()

# Create a variable to store the length of each brick. The width is half
# the length.
brick_length = 40
brick_width = brick_length / 2

# Draw the bricks
# The outer loop's number of iterations is equal to (2 * x) (the total number 
# of rows), so the upper limit for range must be (2 * x + 1), since we're 
# starting from 1, not 0.
for row in range(1, 2 * x + 1):
        
        # This inner loop's number of iterations is equal to y (the total
        # number of bricks in odd-numbered rows), so the upper limit for range
        # must be (y + 1), since we're starting from 1, not 0.
        for brick in range(1, y + 1):
            koopa.forward(brick_length)
            koopa.right(90)
            koopa.forward(brick_width)
            koopa.right(90)
            koopa.forward(brick_length)
            koopa.right(90)
            koopa.forward(brick_width)
            koopa.right(90)
            koopa.forward(brick_length)
        
        # Only execute the following code if the row is even
        # Draw an additional brick for that row
        if (row % 2 == 0):
            koopa.forward(brick_length)
            koopa.right(90)
            koopa.forward(brick_width)
            koopa.right(90)
            koopa.forward(brick_length)
            koopa.right(90)
            koopa.forward(brick_width)
            koopa.right(90)
            koopa.forward(brick_length)
        
        # Once the row is done, reposition the turtle so it is ready to draw
        # the next row
        koopa.penup()
        koopa.right(90)
        koopa.forward(brick_width)
        koopa.right(90)
        koopa.forward(brick_length * y + brick_width)
        koopa.right(180)
        koopa.pendown()         

# The turtle is finished drawing
tscr.mainloop()
turtle.bye()
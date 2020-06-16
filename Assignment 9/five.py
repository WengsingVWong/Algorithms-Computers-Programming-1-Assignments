#******************************************************************************
# five.py
#******************************************************************************
# Name: Wengsing Wong
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# stackoverflow.com
# Mizan Mizan
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
# I attempted the challenge and optimized my program somewhat, but since some
# of them interferes with the test code, I commented out some of them.

class Five:
    """
    A class used to play a Five game
    Attributes: board, empty
    Methods: constructor, .display(), .swap(), .left(), .right(), .up(), 
    .down(), .wins()
    """
    
    # Constructor
    # b is a 2-D list that represents the starting board layout (list of 
    # integers)
    def __init__(self, b):
        self._board = b
        
        for r in range(len(b)):
            for c in range(len(b[r])):
                if (b[r][c] == 0):
                    self._empty = [r, c]
    
    def display(self):
        """Displays the board in a 3-by-2 grid format"""
        for r in range(len(self._board)):
            for c in range(len(self._board[r])):
                if (self._board[r][c] == 0):
                    print("*", end = " ")
                else:
                    print(self._board[r][c], end = " ")
            print()
    
    def _swap(self, pos1r, pos1c, pos2r, pos2c):
        """Swaps the position of any two tiles on the board"""
        temp = self._board[pos1r][pos1c]
        self._board[pos1r][pos1c] = self._board[pos2r][pos2c]
        self._board[pos2r][pos2c] = temp
    
    def left(self):
        """Moves the empty space to the left, if possible (the tile originally 
        there moves to the right)"""
        if self._empty[1] == 0:
            return False
# =============================================================================
#         # Check if 1 and 4 are currently in the leftmost column
#         if (self._board[0][0] == 1 and self._board[1][0] == 4): 
#             is_one_four_col = True                              
#         else:                                                   
#             is_one_four_col = False
# 
#         # Check if 2 and 5 are currently in the middle column
#         if (self._board[0][1] == 2 and self._board[1][1] == 5):
#             is_two_five_col = True
#         else:
#             is_two_five_col = False                            
#         
#         # Check if the empty space is in the middle column when 1 and 4 are in
#         # the leftmost column. If so, do not move 1 or 4.
#         if (is_one_four_col and self._empty[1] == 1): 
#             return False
#         # Check if the empty space is in the rightmost column when 2 and 5 are
#         # in the middle column. If so, do not move 2 or 5.
#         elif (is_two_five_col and self._empty[1] == 2):
#             return False
# =============================================================================
        else:
            self._swap(self._empty[0], self._empty[1], self._empty[0], self._empty[1] - 1)
            self._empty = [self._empty[0], self._empty[1] - 1]
            return True
    
    def right(self):
        """Moves the empty space to the right, if possible (the tile originally
        there moves to the left)"""
        if self._empty[1] == 2:
            return False
        else:
            self._swap(self._empty[0], self._empty[1], self._empty[0], self._empty[1] + 1)
            self._empty = [self._empty[0], self._empty[1] + 1]
            return True
    
    def up(self):
        """Moves the empty space upwards, if possible (the tile originally there
        moves downwards)"""
        if self._empty[0] == 0:
            return False
        
# =============================================================================
#         # Check if 1, 2, and 3 are currently in the top row
#         if (self._board[0][0] == 1 and self._board[0][1] == 2 and self._board[0][2] == 3):
#             is_one_two_three_row = True
#         else:
#             is_one_two_three_row = False
#         
#         # Check if the empty space is in the bottom row when 1, 2, and 3 are in
#         # the top row. If so, do not move 1, 2, or 3
#         if (is_one_two_three_row and self._empty[0] == 1):
#             return False
# =============================================================================
        
        else:
            self._swap(self._empty[0], self._empty[1], self._empty[0] - 1, self._empty[1])
            self._empty = [self._empty[0] - 1, self._empty[1]]
            return True
    
    def down(self):
        """Moves the empty space downwards, if possible (the tile originally
        there moves upwards)"""
        if self._empty[0] == 1:
            return False
        else:
            self._swap(self._empty[0], self._empty[1], self._empty[0] + 1, self._empty[1])
            self._empty = [self._empty[0] + 1, self._empty[1]]
            return True
        
    def wins(self):
        """Checks if the puzzle has been solved"""
        if (self._board == [[1, 2, 3], [4, 5, 0]]):
            return True
        else:
            return False
################################################################################
# PUT YOUR CLASS DEFINITION ABOVE!
################################################################################

# Here are five games. The first two should be easy to solve.
# The last three are harder -- one is impossible!
game1 = [[1,2,0],[4,5,3]]
game2 = [[1,0,2],[4,5,3]]
game3 = [[2,5,4],[1,0,3]]
game4 = [[2,4,5],[1,0,3]]
game5 = [[5,3,1],[0,2,4]]

# I'll use game1 for my test code.


################################################################################
# This code should be uncommented and run
# after you write __init__
################################################################################

print("### TEST 1 ###")
my_puzzle = Five(game1)
print(my_puzzle._board, "(should be [[1, 2, 0], [4, 5, 3]])")
print(my_puzzle._empty, "(should be [0, 2])")


################################################################################
# This code should be uncommented and run
# after you write .display()
################################################################################

print("\n### TEST 2 ###")
my_puzzle.display()

# This should look kind of like
#    1  2  *
#    4  5  3



################################################################################
# This code should be uncommented and run
# after you write ._swap()
################################################################################

print("\n### TEST 3 ###")
print("You should see the 5 and the 1 switch and then switch back: ")
my_puzzle._swap(0,0,1,1)
my_puzzle.display()
print()
my_puzzle._swap(0,0,1,1)
my_puzzle.display()
print()

################################################################################
# This code should be uncommented and run
# after you write .left()
################################################################################

print("\n### TEST 4 ###")
print("You should see the empty space move to the left, followed by True:")
x = my_puzzle.left()
my_puzzle.display()
print(x)
print("You should see the empty space move to the left, followed by True:")
x = my_puzzle.left()
my_puzzle.display()
print(x)
print("You should see the empty space stay where it is, followed by False:")
x = my_puzzle.left()
my_puzzle.display()
print(x)



################################################################################
# This code should be uncommented and run
# after you write .right(), .up(), and .down()
################################################################################

print("\n### TEST 5 ###")
print("You should see the empty space move down, then right, then up:")
my_puzzle.down()
my_puzzle.display()
print()
my_puzzle.right()
my_puzzle.display()
print()
my_puzzle.up()
my_puzzle.display()
print()


################################################################################
# This code should be uncommented and run
# after you write .wins()
################################################################################

print("\n### TEST 6 ###")
print(my_puzzle.wins(), "(should be False)")
my_puzzle.down()
my_puzzle.left()
my_puzzle.up()
my_puzzle.right()
my_puzzle.right()
my_puzzle.down()
print(my_puzzle.wins(), "(should be True -- look at the display below)")
my_puzzle.display()

###############################################################################

# Import the random module in order to use the randrange function
import random

# Main function
def main():
    
    # Put all the games into one list for easy access
    games = [game2, game3, game4, game5]
    
    # Solve each game (or try to solve each game) one-by-one
    for gnum in range(len(games)):
        
        # Create a Five object and initialize an empty move list
        puzzle = Five(games[gnum])
        print("\n\n### GAME {0} ###".format(gnum + 2))
        move_list = []
        
        # Do the first random move. If it fails, repeat until the "first" move 
        # is valid
        while (move_list == []):
            move = random.randrange(1, 5)        
        
            if (move == 1 and puzzle.left()):
                move_list.append("L")
            elif (move == 2 and puzzle.right()):
                move_list.append("R")
            elif (move == 3 and puzzle.up()):
                move_list.append("U")
            elif (move == 4 and puzzle.down()):
                move_list.append("D")
        
        # Make random moves to try to solve the puzzle. Every valid move is
        # appended to a list variable as long as it does not undo the previous
        # move. The loop stops after either the puzzle is solved or after an 
        # excessive number of moves have been made (which likely indicates an 
        # unsolvable puzzle).
        while (puzzle.wins() != True and len(move_list) < 1500):
            move = random.randrange(1, 5)
            
            if (move == 1 and move_list[-1] != "R" and puzzle.left()):
                move_list.append("L")
            elif (move == 2 and move_list[-1] != "L" and puzzle.right()):
                move_list.append("R")
            elif (move == 3 and move_list[-1] != "D" and puzzle.up()):
                move_list.append("U")
            elif (move == 4 and move_list[-1] != "U" and puzzle.down()):
                move_list.append("D")
            
        # Print either the entire list of moves or an error message.
        if (puzzle.wins()):
            for m in move_list:
                print(m, end = "")
        else:
            print("ERROR: This puzzle is unsolvable.")
     
# Run the main function
main()
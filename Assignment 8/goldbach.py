#******************************************************************************
# goldbach.py
#******************************************************************************
# Name: Wengsing Wong
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# Mizan Mizan
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
# I did not attempt the challenge.

def is_prime(num):
    """Returns True if the argument is prime or False if the argument is not
    prime"""
    
    # Initialize a variable to count the number of factors
    nof = 0
    
    # Divide every number between 1 and num into num. For every factor that is
    # found, increment counter by 1.
    for factor in range(1, num + 1):
        if (num % factor) == 0:
            nof += 1
    
    # If num has exactly 2 factors, then it must be prime. If it has less than
    # or more than 2 factors, it is NOT prime.
    if (nof == 2):
        return True
    else:
        return False

def decompose(num):
    """Returns a list containing two prime numbers that add up to the argument
    or containing nothing if there are no two prime numbers that add up to the
    argument"""
    
    # Initialize an empty list that will eventually be returned
    prime_list = []
    
    # stop represents the halfway point between 1 and num
    stop = num // 2
    
    # Check every unique pair of numbers that add up to num, up to and 
    # including the halfway point because after that the pairs will repeat. If 
    # at any point both numbers in the pair are prime, append those numbers to 
    # the list and immediately exit the loop.
    for p in range(1, stop + 1):
        if (is_prime(p) and is_prime(num - p)):
            prime_list.append(p)
            prime_list.append(num - p)
            break
    
    # Return the list (either containing two prime numbers that add up to num
    # or containing nothing)
    return prime_list

# MAIN PROGRAM STARTS HERE

# For every even number between 4 and 800 (inclusive), try to find two prime 
# numbers that add up to it. If there are no two prime numbers that add up to
# it, print an error message. Otherwise, print them out in the form of a 
# mathematical equation.
for even_num in range(4, 801, 2):
    en_pl = decompose(even_num)
    
    if len(en_pl) == 0:
        print("ERROR: {0} cannot be written as the sum of two primes.".format(even_num))
    else:
        print("{0} = {1} + {2}".format(even_num, en_pl[0], en_pl[1]))
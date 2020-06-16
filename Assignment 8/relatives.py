#******************************************************************************
# relatives.py
#******************************************************************************
# Name: Wengsing Wong
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# Monjur Hussan
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
# I did not attempt the challenge.

def dissimilarity(string1, string2):
    """Compares two strings of equal length and returns the dissimilarity 
    between them"""
    
    # Initialize a variable to count the number of dissimilarities
    d = 0
    
    # Compare the strings letter-by-letter. If the characters are not the same,
    # increment the dissimilarity counter. Otherwise, move on to the next pair
    # of letters.
    for i in range(len(string1)):
        if (string1[i] != string2[i]):
            d += 1
    
    # Return the final dissimilarity counter
    return d

# MAIN PROGRAM STARTS HERE

# Read the dna file and store its contents in a variable as a list
dna_file = open("dna.txt", "r")
dna_list = dna_file.read().split()
dna_file.close()

# Initialize a variable to store the minimum dissimilarity value. 100 is the
# maximum possible value for this variable.
dissim = 100

# Compare each string with every other string in the list. The outer loop will
# go from 0 to 198, representing the first string (#1 to #199) to be compared, 
# while the inner loop will go from 1 to 199, representing the second string 
# (strings #2 to #200) to be compared.
for i in range(len(dna_list) - 1):
    for j in range(i + 1, len(dna_list)):
        
        # Calculate the dissimilarity between each pair of strings
        d = dissimilarity(dna_list[i], dna_list[j])

        # If the calculated value is less than the current minimum
        # dissimilarity, set the calculated value as the new minimum
        # dissimilarity. Also, overwrite the current contents of the variables
        # holding the strings and their line numbers with the corresponding
        # values associated with this pair of strings.
        if (d < dissim):
            dissim = d
            string1 = dna_list[i]
            string2 = dna_list[j]
            s1_line = i + 1
            s2_line = j + 1

print("Here are the strings with the least dissimilarity:")
print("{0} (Line {1})".format(string1, s1_line))
print("{0} (Line {1})".format(string2, s2_line))
print("Dissimilarity Value:", dissim)
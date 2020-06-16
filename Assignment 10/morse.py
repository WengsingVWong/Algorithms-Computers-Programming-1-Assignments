#******************************************************************************
# morse.py
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
#

def create_md():
    """Creates and returns a dictionary containing English-to-Morse-code 
    translations"""
    
    # Open the text file containing the translations in reading mode
    morse_file = open("morse.txt", "r")

    # Initialize an empty dictionary
    md = {}

    # For each line in the file, break it into two parts: the English part and
    # the Morse code part. Add both to the dictionary so that English part is 
    # the key and the Morse code part is the corresponding value. 
    for line in morse_file:
        chars = line.split()
        md[chars[0]] = chars[1]

    # Add a Morse code translation for spaces
    md[" "] = "/"
    
    # Close the text file
    morse_file.close()
    
    # Return the morse code dictionary
    return md

def get_user_file():
    """Opens a text file of the user's choice and returns the file object"""
    
    # Flag to store whether the user has inputted a valid text file name
    does_fname_exist = False

    # Ask user to enter the name of a text file
    tfname = input("Enter the name of a text file: ")

    # Validate user input
    # Repeat the loop until the user enters a valid text file name
    while (not does_fname_exist):
        try:
            ufile = open(tfname, "r")
            does_fname_exist = True
        except FileNotFoundError:
            tfname = input("That file does not exist. Please enter the name of an existing text file: ")
    
    # Return the file object
    return ufile

def morse(engfile, trans_dict):
    """Translates the contents of an English text file to Morse code and prints
    them to the screen"""
    
    print("Here is your file translated into Morse code:")
    
    # Translate the contents of the text file one character at a time
    while True:
        
        # Read 1 character from the file
        one_char = engfile.read(1)
        
        # If the end of the file is reached, stop reading
        if not one_char:
            break
        
        # Try to translate each character in the file. If there is no Morse 
        # code equivalent, print an "x"
        try:
            print(trans_dict[one_char], end = " ")
        except KeyError:
            print("x", end = " ")

def main():
    
    # Create the Morse code dictionary
    morse_dict = create_md()
    
    # Open the file to be translated in reading mode
    user_file = get_user_file()
    
    # Translate the contents of the file to Morse code
    morse(user_file, morse_dict)
    
    # Close the file
    user_file.close()

main()
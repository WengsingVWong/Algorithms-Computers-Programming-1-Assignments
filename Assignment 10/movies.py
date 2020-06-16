#******************************************************************************
# movies.py
#******************************************************************************
# Name: Wengsing Wong
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# Mizan Mizan
# stackoverflow.com
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

# Import the pandas module in order to read data from a CSV file
import pandas as pd

# Initialize an empty dictionary
zip_count = {}

# Read the data from a CSV file into a DataFrame object
permits_df = pd.read_csv("permits.csv")

# Ask user to input a month and year and retrieve them
month_year = input("Please enter a month and a year, separated by a space: ")
m_y_split = month_year.split()
month = int(m_y_split[0])
year = int(m_y_split[1])

# Create a column indicating which rows meet the following criteria: 
# the event type is a Shooting Permit, and the month and year are the month and
# year entered by the user
user_data = (permits_df["EventType"] == "Shooting Permit") & (permits_df["Month"] == month) & (permits_df["Year"] == year)

# Create a smaller DataFrame object containing only the rows that match the
# above criteria
user_df = permits_df[user_data]

# Count the zip codes
# Convert each row of zip codes into a list and split it to access each
# individual zip code. Then track the number of times each zip code appears
# using a dictionary, adding new keys if the zip codes do not yet exist.
# If a row does not contain a zip code for whatever reason, skip that row.
for idx, r in user_df.iterrows():
    
    try:    
        zip_list = r["ZipCode"].split()
    
        for zc in zip_list:
            try:
                zip_count[zc] += 1
            except KeyError:
                zip_count[zc] = 1
                
    except AttributeError:
        print("Row {0} does not contain a zip code. Proceeding to skip...".format(idx))

# Store all of the zip code counts as a list and determine which is the greatest
zc_freq = list(zip_count.values())
max_zc_freq = max(zc_freq)

# Create an empty list to store the zip code(s) that appear(s) the most
# frequently
max_zc = []

# Determine which zip code(s) appear(s) the most frequently
for zc in zip_count:
    if (zip_count[zc] == max_zc_freq):
        max_zc.append(zc)

# Print out the zip code(s) that appear(s) the most frequently
if (len(max_zc) > 1):
    print("The zip codes that appear most frequently are:")
    
    for zc in max_zc:
        print(zc)
else:
    print("The zip code that appears most frequently is:", max_zc[0])
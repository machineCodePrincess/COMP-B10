#-----------------------------------------------------------------------
# Program name: Assignment 3 
# Author: Sarena Cerda
# Date: 9/21/16
# Purpose: Get polling station information for of age voters living in correct zipcodes.
#-----------------------------------------------------------------------
# GLOBAL VARIABLE DEFINITIONS (Use only until functions)
#
# int: age, zipCode

#-----------------------------------------------------------------------
# CONSTANT DEFINITIONS

#-----------------------------------------------------------------------
# CLASS DEFINITIONS

#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC
#

print("VOTER ELIGIBILITY AND POLLING STATION PROGRAM")

age = 1

while age > 0:
    age = int(input("\n\nEnter you age (Type '0' to exit program): "))
    if(age > 17 and age != 0):
        zipCode = int(input("\n\tEnter your residence\'s zip code: "))

        if zipCode == 93305:
            print("\tYour polling station is 123 Panorama Drive.")
        elif zipCode == 93306:
            print("\tYour polling station is 6143 Fairfax Drive.")
        elif zipCode == 93307:
            print("\tYour polling station is 21121 B Street.")
        elif zipCode == 93308:
            print("\tYour polling station is 863 Desmond Ct.")
        elif zipCode == 93309:
            print("\tYour polling station is 7332 Del Canto Ct.")
        else:
            print("\tError - unknown zip code.")
    elif (age < 18 and age != 0):
        print("\n\tYOU ARE INELIGIBLE TO VOTE.")
        
    
input("\nRun complete. Press the Enter key to exit.")

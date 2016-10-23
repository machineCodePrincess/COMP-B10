#-----------------------------------------------------------------------
# Program name: Assignment 2
# Author: Sarena Cerda
# Date: 9/17/16
# Purpose: Take user input for conversions (if valid input). print out the conversion.
#-----------------------------------------------------------------------
# GLOBAL VARIABLE DEFINITIONS (Use only until functions)
#
# float: fahrenheit, celsius, miles, kilometers, pounds, kilograms
# string: option

#-----------------------------------------------------------------------
# CONSTANT DEFINITIONS

#-----------------------------------------------------------------------
# CLASS DEFINITIONS

#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC
#


print("CONVERSION PROGRAM\n\n")
print('T = Convert Fahrenheit to Celsius \nD = Convert Miles to Kilometers \nW = Convert Pounds to Kilograms\n')


option = (input("Select conversion to perform ('T'emperature, 'D'istance, 'W'eight)? "))
print()

if (option == 'T' or option == 't') :
	fahrenheit = float(input("Please enter the temperature in FAHRENHEIT: "))
	celsius = (fahrenheit - 32) / 1.8
	print(fahrenheit, "fahrenheit is", format(celsius, '.3f'), "celsius.")
	
elif (option == 'D' or option == 'd'):
	miles = float(input("Please enter the distance in MILES: "))
	kilometers = miles / 0.621371192237
	print(miles, "miles is", format(kilometers, '.3f'), "kilometers.")
	
elif (option == 'W' or option == 'w'):
	pounds = float(input("Please enter the weight in POUNDS: "))
	kilograms = pounds / 2.2
	print(pounds, "pounds is", format(kilograms, '.3f'), "kilograms.")
else :
        print("Error - Invalid option selected. You may only enter T, D, or W.")



input("\nRun complete. Press the Enter key to exit.")


# Rectangle Area and Perimeter Calculator

# This program calculates and displays the area and perimeter of a rectangle based on user input.
# Importing from a custom module named 'calculate' that contains functions to calculate area and perimeter.


import calculate # calculate.py is in the same directory

length = float(input("Enter the length of the rectangle: ")) # input from the user
width = float(input("Enter the width of the rectangle: ")) # input from the user

area = calculate.area(length, width) # calculate the area
perimeter = calculate.perimeter(length, width) # calculate the perimeter

print("The area of the rectangle is", area) # print the area
print("The perimeter of the rectangle is", perimeter) # print the perimeter

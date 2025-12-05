# Exception Handling Example This program demonstrates basic exception handling in Python

# Basic Exception Handling Example wih undefined variable

try: # This block of code may raise an exception
    print (x)  # This should print x but will not. This will raise a NameError since x is not defined
except NameError: # This block of code will execute if a NameError occurs
    print("Please define the variable x before running this code.") # If an exception occurs, this message will be printed
except: # This block will catch any other exceptions that are not specifically handled
    print( "An exception occurred") # This will print a generic message indicating an exception occurred
    
# Variable Assignment Example defining a variable and printing it
x = 5
if x > 0:  # Check if x is greater than 0
    print("x is positive")  # If true, print this message
elif x == 0:  # Check if x is equal to 0
    print("x is zero")  # If true, print this message
else:  # If x is not greater than 0 or equal to 0
    print("x is negative")  # If true, print this message
    
# Exception Handling Example with user input and division
# This code will prompt the user for input and handle potential exceptions like division by zero or invalid

# try:
#     numerator = float(input("Enter the numerator: "))
#     denominator = float(input("Enter the denominator: "))
#     result = numerator / denominator
#     print("The result is", result)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Invalid input. Please enter numeric values.") 
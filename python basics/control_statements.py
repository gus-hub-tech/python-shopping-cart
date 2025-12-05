# What are control statements in Python?
# Control statements in Python are constructs that allow you to control the flow of execution of your program based on certain conditions. They enable you to make decisions, repeat actions, and manage the execution path of your code. The main types of control statements in Python include:# 1. **Conditional Statements**: These statements allow you to execute certain blocks of code based on whether a condition is true or false. The primary conditional statements are:
#    - `if`: Executes a block of code if the condition is true.
#    - `elif`: Executes a block of code if the previous conditions were false and the current condition is true.
#    - `else`: Executes a block of code if none of the previous conditions were true.

# Example of a conditional statement:
num = -1
if num > 0:
    print("The number is positive.")
    # Code to execute if condition is true
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")
    
# # Control statements in Python -- More!

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print("The first number is greater than the second number.")
elif num1 < num2:
    print("The second number is greater than the first number.")
else:
    print("Both numbers are equal.")
# Control statements in Python are constructs that allow you to control the flow of execution of your program based on certain conditions. They enable you to make decisions, repeat actions, and manage the execution path of your code. The main types of control statements in Python include:


# 2. **Looping Statements**: These statements allow you to repeat a block of code multiple times. The primary looping statements are:
#    - `for`: Iterates over a sequence (like a list, tuple, or string) and executes a block of code for each item in the sequence.
#    - `while`: Repeats a block of code as long as a specified condition is true.

# Example of a looping statement:
for color in ["black", "green", "yellow", "pink", "red", "maroon", "purple", "orange", "brown", "white", "blue"]:
    print("Iteration:", color)
    # Code to execute in each iteration
i = 5
while i < 10:
    print("While loop iteration:", i)
    i += 5
    # Code to execute while condition is true

# Using the while loop to print numbers from 1 to 5
i = 1
while i <= 5:
    print("While loop iteration:", i)
    i += 1 # Increments the value of i by 1 in each iteration


# 3. **Control Flow Statements**: These statements alter the flow of execution within loops or conditional blocks. The primary control flow statements are:
#    - `break`: Exits the nearest enclosing loop prematurely.
#    - `continue`: Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
#    - `pass`: Does nothing; it is a placeholder that allows you to write empty blocks of code.

# Example of control flow statements:
for i in range(5):
    if i == 2:
        print("Skipping iteration 2")
        continue  # Skips the rest of the loop for this iteration
    elif i == 4:
        print("Breaking out of the loop at iteration 4")
        break  # Exits the loop
    print("Iteration:", i)
#    - `pass`: A null statement that does nothing; it is used as a placeholder.


# 4. **Exception Handling Statements**: These statements allow you to handle errors and exceptions gracefully. The primary exception handling statements are:
#    - `try`: Defines a block of code to be tested for errors.
#    - `except`: Defines a block of code to be executed if an error occurs in the try block.
#    - `finally`: Defines a block of code that will be executed regardless of whether an error occurred or not.
#    - `raise`: Used to raise an exception manually.
# These control statements are essential for creating dynamic and responsive programs in Python, allowing you to implement complex logic and handle various scenarios effectively.


# Project description: A simple shopping cart program with notes.

# Create a shopping cart programme that will continuously ask the user for a food product and the price of that product.
# Have an exit clause if the user wishes to stop adding more things to their cart.
# At the end show the food items and the total cost to the user.

# Initialize lists and variables

foods = [] # List to store food items
prices = [] # List to store prices of food items
cost_total = 0.0 # Variable to store total cost

# Welcome message!
print("Welcome to the Shopping Cart Program!")  # Welcome message

# Continuously ask for food items and prices-Loop used and if else statement to check for exit condition

while True: # Start an infinite loop to continuously ask for input
    # Ask user for food item and price
    food = input("Enter a food product (or type 'exit' to finish): ") # Input food item and check for exit condition

    if food == 'exit': # Check if user wants to exit
        break  # Exit the loop if user types 'exit'
    else: # Ask for price of the food items
        price = float(input(f"Enter the price of {food}: R")) # Input price of the food item and display item value in South African Rand (R)
        foods.append(food) # Append food item to the list
        prices.append(price) # Append price to the list
        cost_total += price # Add price to total

# Display the shopping cart items and prices values.
print("-----Your CART-----") # Display shopping cart items and prices.

for food, price in zip(foods, prices): # Iterate through the lists of food items and prices
    print(f"{food} - R{price:.2f}") # Display each food item and its price in South African Rand (R) with 2 decimal places.
    
print("\n") # Leave a blank line for better readability
print(f"Total cost: R{cost_total:.2f}") # Display the total cost in South African Rand (R) with 2 decimal places.
print("-----End of CART-----") # Display shopping cart items and prices.


# End of the shopping cart program
print("Thank you for using the Shopping Cart Program!")  # Thank you message
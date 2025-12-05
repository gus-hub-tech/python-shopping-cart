# Python Shopping Cart Application

## Description

This is a simple Python command-line program that simulates a shopping cart. The user can add food products and their prices to the cart, and when finished, the program displays all items with their prices and the total cost. All prices are displayed in South African Rand (R) with proper formatting.

## Project Structure

```
python-shoppingcart-app9/
├── shopping_cart.py          # Main shopping cart program
├── python basics/            # Python learning exercises
│   ├── rectangle_calculator/ # Rectangle calculation module
│   └── [various .py files]  # Basic Python concept examples
├── variables.py              # Variable examples
└── README.md                # This file
```

## How It Works

1. **Start the Program:**  
   The program welcomes the user and starts an infinite input loop.

2. **Add Items:**  
   The user is prompted to enter the name of a food product.  
   - If the user types `exit`, the program stops asking for more items.
   - Otherwise, the user is prompted to enter the price with "R" prefix for South African Rand.

3. **Store Data:**  
   - Each food item is added to a `foods` list.
   - Each price is added to a `prices` list.
   - The total cost is accumulated in `cost_total` variable.

4. **Display Cart:**  
   After the user exits, the program prints:
   - A formatted cart header
   - All food items with their prices (formatted to 2 decimal places)
   - A blank line for readability
   - The total cost (formatted to 2 decimal places)
   - A cart footer

5. **End Message:**  
   The program thanks the user for using the shopping cart.

## Example Usage

```
Welcome to the Shopping Cart Program!
Enter a food product (or type 'exit' to finish): Bread
Enter the price of Bread: R12.50
Enter a food product (or type 'exit' to finish): Milk
Enter the price of Milk: R18.00
Enter a food product (or type 'exit' to finish): exit
-----Your CART-----
Bread - R12.50
Milk - R18.00


Total cost: R30.50
-----End of CART-----
Thank you for using the Shopping Cart Program!
```

## Technical Implementation

- Uses Python lists to store food items and prices
- Implements a `while True` loop for continuous input
- Uses `zip()` function to iterate through paired lists
- Formats currency with `.2f` for consistent decimal places
- Handles user input validation for exit condition

## Requirements

- Python 3.x

## How to Run

1. Navigate to the project directory:
   ```bash
   cd /path/to/python-shoppingcart-app9
   ```

2. Run the main shopping cart program:
   ```bash
   python shopping_cart.py
   ```

## Features

- Add unlimited food items to your cart
- Real-time total cost calculation
- South African Rand (R) currency formatting
- Clean, formatted cart display
- Simple exit mechanism
- Input validation and error handling

## Additional Learning Materials

This project also includes a `python basics/` directory with various Python learning exercises covering:
- Basic data types and operators
- Control statements and loops
- Data structures (lists, dictionaries, sets, tuples)
- Exception handling
- Modules and built-in functions
- String manipulation

---

# Dictionaries are a collection of key-value pairs.
# Each key is unique and maps to a value. Dictionaries are mutable, meaning you can change their content after creation.
# They are unordered, meaning the items do not have a defined order.
# Keys must be immutable types (like strings, numbers, or tuples), while values can be of any type.
#It can be a string or a numeric data type.
#Defiend using curly braces {} or the dict() constructor.

# Example of a dictionary in Python
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values in a dictionary via keys and the square brackets.

print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(my_dict["name"])  # Output: Alice value
print(my_dict["age"])  # Output: 30 value
print(my_dict["city"])  # Output: New York value

# Changing values in a dictionary - mutability
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}


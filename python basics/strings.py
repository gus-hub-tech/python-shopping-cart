# Strings are immutable sequences of characters in Python.
# They can be created using single quotes, double quotes, or triple quotes for multi-line strings.

# Example of creating strings
single_line = 'Hello, World!'
double_line = "Hello, World!"
multi_line = '''This is a
multi-line string.'''

# Strings 
message = "Python is fun!"
print(message)  # Output: Python is fun!

# Strings on multiple lines
message = '''Python is fun!
It is easy to learn.
Let's start coding!'''
print(message)

# String concatenation
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)  # Output: Hello, Alice!

# Stringgs can be indexed - indexing with strings starts at 0
message = "Hello, World!"
print(message[0])  # Output: H
print(message[1])  # Output: e
print(message[2])  # Output: l
print(message[3])  # Output: l
print(message[4])  # Output: o
print(message[5])  # Output: ,
print(message[6])  # Output:  
print(message[7])  # Output: W
print(message[8])  # Output: o
print(message[9])  # Output: r
print(message[10])  # Output: l
print(message[11])  # Output: d
print(message[12])  # Output: !

# Strings can be indexed from the end using negative indices
print(message[-1])  # Output: !
print(message[-2])  # Output: d
print(message[-3])  # Output: l


# String length counts each character, including spaces and punctuation
message = "Hello, World!"
print(len(message))  # Output: 13 (length of the string)
# What is string manipulation in Python?

# String manipulation in Python refers to the various operations and methods that can be applied to strings to modify, analyze, or extract information from them.
# It includes operations like changing case, stripping whitespace, replacing text, splitting strings, and joining strings.

# String manipulation examples

# Changing case
message = "Hello, World!"
print(message.upper())  # Output: HELLO, WORLD!
print(message.lower())  # Output: hello, world!

# Stripping whitespace
message = "   Hello, World!   "
print(message.strip())  # Output: Hello, World!

# Replacing text
message = "Hello, World!"
print(message.replace("World", "Python"))  # Output: Hello, Python!

# Splitting strings
message = "Hello, World!"
print(message.split(","))  # Output: ['Hello', ' World!']

# Joining strings
words = ['Hello', 'World!']
print(" ".join(words))  # Output: Hello World!

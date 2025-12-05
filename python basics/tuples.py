# Tuples are a collection of objects that are ordered and immutable.
# Orderd means that the items have a defined order and can be accessed by their index.[similar to lists]
# Immutable means that the items cannot be changed, added, or removed after the tuple is created.

my_tuple = ("blue", "green", "red", "yellow", "white", "black")
print(my_tuple)

 #Tuples can contain different data types with normal indexing and negative indexing.
 
print(my_tuple[0]) # Accessing the first element of the tuple
print(my_tuple[1]) # Accessing the second element of the tuple
print(my_tuple[2]) # Accessing the third element of the tuple
print(my_tuple[3]) # Accessing the fourth element of the tuple
print(my_tuple[4]) # Accessing the fifth element of the tuple


print(my_tuple[-5]) # Accessing the first element of the tuple using negative indexing
print(my_tuple[-2]) # Accessing the last element of the tuple using negative indexing

#Tupels can be concatenated using the + operator.

tuple1 = ("red")
tuple2 = ("rose")

conc_tupel = tuple1 + tuple2
print(conc_tupel)  # Output: redrose 

# Tuples can be repeated using the * operator.

repeat_tupel = tuple1 * 3
print(repeat_tupel)  # Output: redredred

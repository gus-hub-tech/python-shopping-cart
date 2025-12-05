#A set in Python is an unordered collection of unique items. 

# #Unordered - The items do not have a defined order.
# #Unique - Duplicate values are not allowed.

#Note ''' Are used to comment out multiple lines in Python, similar to the # symbol.

'''
my_set = {1, 2, 3, 4, 5}
print(my_set) # Output: {1, 2, 3, 4, 5}

my_set.add(6) # Adding an element
print(my_set) # Output: {1, 2, 3, 4, 5, 6}

my_set.remove(3) # Removing an element
print(my_set) # Output: {1, 2, 4, 5, 6}

'''

#Operations with set union 
set_a = {1, 2, 3}
set_b = {3, 4, 5}

set_union = set_a.union(set_b) # Union of two sets
print(set_union) # Output: {1, 2, 3, 4, 5} note duplicate 3 is not included

#Operations with set intersection
set_intersection = set_a.intersection(set_b) # Intersection of two sets
print(set_intersection) # Output: {3} note only common element is included, this finds common elements in both sets wich is 3

#Operations with set difference
set_difference = set_a.difference(set_b) # Elements in set_a but not in set_b
print(set_difference) # Output: {1, 2} note only elements in set_a , this finds elements that are in set_a but not in set_b


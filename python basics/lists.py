# This is a normal Python file that contains a list of fruits and prints it.
fruits = ["apple", "banana", "cherry", "elderberry"]
print(fruits)

# This is a normal Python file that contains a list of vegetables and prints it, thes values are changable.
vegetables = ["carrot", "broccoli", "spinach", "potato"]
print(vegetables[0]) # Print the first vegetable in the list, through its index. [e.g. 0 for the first item, 1 for the second item, etc.]

# This is a normal Python file that contains a list of animals and prints it, thes list values are mutable,[meaning they can be changed].
animals = ["dog", "cat", "rabbit", "hamster"]
print(animals)
animals[0] = "monkey"  # Changed the first in the list
print(animals)

# This is a normal Python file that contains a list of values that will be added and removed. [There are vatious methods to do this]
brands = ["Nike", "Adidas", "Puma", "Reebok"]
brands.append("Under Armour")  # Adding a new brand to the list
print(brands)

brands.remove("Puma")  # Removing a brand from the list
print(brands)

# This is a normal Python file that contains a list of vaulues that will be sorted.
cars = ["Toyota", "Honda", "Ford", "BMW"]
cars.sort()  # Sorting the list of cars in alphabetical order, the lsit can be sorted in reverse order by using the reverse parameter[advanced stuff.]
print(cars)

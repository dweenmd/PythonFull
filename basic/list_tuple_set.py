                # Lists (denoted by square brackets [])
                # Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements of a list
print(my_list[0])  # Output: 1

# Modifying elements of a list
my_list[1] = 10
print(my_list)  # Output: [1, 10, 3, 4, 5]

# List comprehension
squared_numbers = [x**2 for x in range(1, 6)]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]




                # Tuples (denoted by parentheses ())
                # Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements of a tuple
print(my_tuple[0])  # Output: 1

# Tuples are immutable, cannot be modified
# my_tuple[1] = 10  # This will raise a TypeError

# Tuple unpacking
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # Output: 1 2 3 4 5



                # Sets (denoted by curly braces {})   NO duplicate
                # Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements to a set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements from a set
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Set operations (e.g., union, intersection)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}
print(intersection_set)  # Output: {3}

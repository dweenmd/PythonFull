#list compreshension = A concise way to create lists in python 
#                        compact and easier to read than traditional loops
#                       [expression for value in iterable if condition ]
#                       [expression for item in iterable]


doubles = []
for x in range(1,11):
    doubles.append(x*2)
print(doubles)

# Example 1: List of squares of numbers
squares = [x**2 for x in range(11)]
print("Squares:", squares)
double = [x*2 for x in range(1,11)]
print("Double:", double)
triples = [x*3 for x in range(1,11)]
print(f"Tripples: {triples}")

#example 2: 
fruits=["apple","orange","banana","coconut"]
fruits=[]


# Example 3: List comprehension with condition (if clause)
#     [expression for value in iterable if condition ]
even_numbers = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", even_numbers)
# Output: [0, 2, 4, 6, 8]

# Example 4: Nested list comprehension
pairs = [(x, y) for x in range(3) for y in range(3)]
print("Pairs:", pairs)
# Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# Example 5: Multiple conditions
filtered = [x for x in range(10) if x % 2 == 0 and x > 4]
print("Filtered even numbers greater than 4:", filtered)
# Output: [6, 8]

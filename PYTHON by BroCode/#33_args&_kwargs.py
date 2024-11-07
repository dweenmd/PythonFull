# *args     =allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple keyword arguments
#           * unpacking operator
#           1.positional 2.default 3.keyword 4. ARBITARY


# Example of *args (Positional Arguments)
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

# Calling add function with multiple positional arguments
x = add(1, 2, 3, 4, 5, 6)
print("Positional Arguments:")
print(f"Sum: {x}") 


# Example of **kwargs (Keyword Arguments)
print("Keyword Arguments:")
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key:10}: {value}")

# Calling print_address with multiple keyword arguments

print_address(street="123 Fake St.",
              city="Detroit",
              state="MI",
              zip="54321")


# Example of using both *args and **kwargs together
print()
print("Keyword & positional arguments:")
print()
def shipping_level(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print() 
    
    for key, value in kwargs.items():
        print(f"{key:10} : {value}")
        



# Calling describe_person with both positional and keyword argumentsdescribe_person("John", "Doe", age=30, occupation="Engineer", country="USA")
shipping_level("Dr","Spongebob","Squarepants","III",
              street="123 Fake St.",
              apartment="100",
              city="Detroit",
              state="MI",
              zip="54321")

# Example of unpacking using * and **
def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

# Unpacking a list into *args
person_data = ["Alice", 25]
greet(*person_data)  # Output: Hello, Alice. You are 25 years old.

# Unpacking a dictionary into **kwargs
person_info = {"name": "Bob", "age": 40}
greet(**person_info)  # Output: Hello, Bob. You are 40 years old.

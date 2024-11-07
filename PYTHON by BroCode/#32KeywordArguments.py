# keyword arguments = an argument preceded by an indentifire helps with
#                     readability order of arguments doesn't matter
#                     1. positional 2.default 3.keyword 4.arbitrary

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

# Using keyword arguments
greet(name="Alice", age=30)
greet(age=25, name="Bob")  #this is key word arguments


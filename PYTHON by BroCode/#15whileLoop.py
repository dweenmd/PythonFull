#while loop = Excecute some code while some conditions remains true 

age = int (input(f"Enter your age: "))

while age<0:
    print("Age cannot be negative.")
    age = int (input(f"Enter your age: "))

print(f"You are {age} years old.")
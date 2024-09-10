# input() = A function that prompts the user to enter data 
#          returns the entered data as a string

name = input("what is your name? " )
age= input("How old are you? ")

#age should be in integer formate so we have to type cast it 
age=int(age)
age=age+1

print(f"Hello {name}!")
print(f"You are {age} years old.")
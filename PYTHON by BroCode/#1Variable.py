#variable = A container for a value (string , integer, float ,boolean)
#           A variable behaves as if it was the value it contains.


#Strings 
first_name="dween"
food ="pizza"
email="dween@fake.com"

print(f"Hello {first_name}")
print(f"You like {food}")
print (f"Your email: {email}")

#Integer 
age =25
quantity = 3
num_of_students= 25

print(f"You are {age} years old")
print (f"you are buying {quantity} pens")
print(f"Total students of the class {num_of_students}")

#Float
price=10.99
gpa=3.5
distance=5.5

print(f"price {price}, per unit")
print(f"your gpa is {gpa}")
print(f"total walking distance is : {distance}")

#Boolean
is_student=False

if is_student:
    print("you are a student")
else :
    print("You are not a student")
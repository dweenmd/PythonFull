#conditional expression = A one line shorcut for the if else statement ( rernary operator)
#                        print or assign one of two values based on a condition
#                        x if condition else Y
num = 6
a=6
b=7

#print("Positive" if num>0 else "negetive")
#result= "Even" if num%2 ==0 else "000"

max_num = a if a>b else b
min_num= a if a<b else b

print(min_num)

age =25
status= "Adult" if age>= 18 else "Child"
print(status)
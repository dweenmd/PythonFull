print("Enter 2 number: ")
a=float (input())
b=float(input())
print ("Select the operator '+', '-', '*', '/' ")
op=input()
if op=='+':
    print(f"Summetion of {a} and {b} is : {a+b} ")
elif op=='-':
    print(f"Substraction of {a} and {b} is: {a-b}")
elif op=='/':
    print(f"Division of {a} and {b} is: {a/b}")
else:
    print(f"Multiplication of {a} and {b} is: {a*b}")
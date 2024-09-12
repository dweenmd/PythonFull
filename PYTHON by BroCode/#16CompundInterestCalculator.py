#compund interest calculator 

principal =0
rate =0 
time=0

while principal<=0:
    principal=float(input("Enter the principal ammount: "))
    if principal<=0:
        print("Principal cann't be less than or equal zero.")

while rate<=0:
    rate=float(input("Enter the rate ammount: "))
    if rate<=0:
        print("Rate cann't be less than or equal zero.")

while time<=0:
    time=int(input("Enter the time in Year : "))
    if time<=0:
        print("Time cann't be less than or equal zero.")
total = principal* pow((1+rate/100),time)
print (f"Blalnce after {time} years: ${total:,}")


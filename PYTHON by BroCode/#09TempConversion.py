unit=input("Is this temperature in celcius or fahrenheit (C/F)?")
temp = float(input("Enter the temperature:"))

if unit =='C' or 'c':
    temp=round((9*temp)/5+32,1)
    print(f"The temperature in Fahrenheit is: {temp} degree")
elif unit=='F' or 'f':
    temp=round((temp-32)*5/9,1)
    print(f"The temperature in celsius is: {temp} degree") 
else:
    print(f"{unit} is an invalid unit of measurment")
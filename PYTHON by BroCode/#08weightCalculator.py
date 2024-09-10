
weight=float(input("Enter your weight: "))
unit= input("kilograms or pounds? (K or L)")
if unit=='k':
    weight =weight*2.205
    unit ="LBS."
    print(f"Your weight is: {round(weight,1)} {unit}")

elif unit=='l':
    weight=weight/2.205
    unit="kgs."
    print(f"Your weight is: {round(weight,1)} {unit}")

else:
    print(f"{unit} was not valid")


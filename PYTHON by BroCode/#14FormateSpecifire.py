#formate spacifiers= {value: flags} formate a value based on what flags are inserted

#    :(number)f = round to that many decimal places (fixed point)
#    :(number)  = alocate that many spaces
#    :03 = alocate and zero pad that many spaces
#    :< = left justify
#    :> = right justify
#    :^ = center align
#    :+ = use a plus sing to indicate positive value
#    := = place sing to leftmost position
#    :  = insert a space before positive numbers
#    :, = comma separator


price1= 3.14159
price2= -987.65
price3= 12.63

print(f"price 1 is ${price1: .2f}")
print(f"price 2 is ${price2: .2f}")
print(f"price 3 is ${price3: .2f}")
print(" ")

print(f"price 1 is ${price1:10}")
print(f"price 2 is ${price2:10}")
print(f"price 3 is ${price3:10}")
print(" ")

print(f"price 1 is ${price1:<}")
print(f"price 2 is ${price2:>2f}")
print(f"price 3 is ${price3:<}")
print(" ")

print(f"price 1 is ${price1:+}")
print(f"price 2 is ${price2:+}")
print(f"price 3 is ${price3:+}")

print("......................")
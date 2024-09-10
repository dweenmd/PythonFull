#logical operators = evaluate multiple coditions(or ,and ,not)
#                or  = at least one condition must be true
#                and = both condition must be true
#                not = inverts the condition(not False, not True)


temp =30 
is_raining=False
is_sunny=True

#example of or
if temp>35 or temp<0 or is_raining:
    print("the outdoor event is cancelled")
else:
    print (" The outdoor event is still scheduled ")

#Example of and
if temp>=28 and is_sunny:
    print("It is hot outside🥵")
    print("It is sunny☀️")
elif temp<=0 and is_sunny:
    print("It is cold outside🥶")
    print("it is sunny☀️")
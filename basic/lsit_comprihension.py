numbers=[45,80,65,43,76,86,48,85,34,61]
odds=[]
for num in numbers:
    if(num%2!=0 ):
        odds.append(num)

print(odds)

even_num=[num for num in numbers if num%2==0]
print(even_num)
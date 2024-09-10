# list, array, collection is same (simple terms)

# index =  0   1   2   3   4    5   6   7   8  9
numbers = [45, 67, 56, 40, 55, 23, 66, 78, 90, 10]
# index=   -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
print(numbers[3], numbers[-3])

# list(start:end)  start form start index and stop before the end index
print(numbers[2:6])

# list(start: end: step)
print(numbers[1:7:2])  # 2step kore agabe

print(numbers[1:7:1])
print(numbers[6:0:-1])  # ulta print hobe

# other cases
print(numbers[4:])  # by defult 4 index theke suru kore sesh porjonto
print(numbers[:6])  # by defult 0 index thk suru kore 5 inddex porjonto

print('full array print',numbers[:])
print ('full array reverse: ',numbers[::-1])
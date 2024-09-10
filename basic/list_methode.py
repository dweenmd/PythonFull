# https://docs.python.org/3/tutorial/datastructures.html
numbers = [12, 44, 98, 68, 78, 56]
numbers.append(56)
print(numbers)
numbers.insert(2, 71)  # 2 no index e 71 insert
print(numbers)
# remove any number
if 98 in numbers:
    numbers.remove(98)
if 8 in numbers:
    numbers.remove(8)
print('after removing number:', numbers)
numbers.sort()
print('sorted array', numbers)
numbers.reverse()
print('reverse:', numbers)

# enumarate
# for printing index and value of a list /array
for i, num in enumerate(numbers):
    print("index:", i, "->", num)

# example of define or def or function
def sum(num1, num2):
    result = num1+num2
    return result


total = sum(44, 56)
print(total)
a = 5
print(a)

# example of args
print("example of args")


def total_elm(*numbers):
    print(numbers)
    sum = 0  # Initialize sum to 0
    for num in numbers:
        print(num)
        sum += num  # Increment sum by num
    return sum


# joto songkha deya hok na keno somossa nai
total = total_elm(45, 46, 89, 11, 89)
print("total elements:", total)


def full_name(first,last):
    name=f'fullname is: {first} {last}'
    return name
# take perameter in order (serial order)
# name=full_name('dween', 'mohammad')
name = full_name(last='mohammad', first='dween')
print(name)

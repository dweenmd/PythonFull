#iterables = An object/collection that can return its elements one at a time , allowing it to be iterated over in a loop
#list [] is reversable---> iterables
#tupple () is reversable---> iterables
#Dictonaries {} is ir-reversable---non-iterables

numbers=[1,2,3,4,5,6] 

for number in numbers:
    print(number)

for number in reversed(numbers):
    print(number)

collections={"Mango", "Banana","Orange","Pineapple"} #set is ir-reversable---iterables(cannot reverse a set because there is no inherent order to reverse.)
for collection in collections:
    print(collection)
# for collection in reversed(collections):   # Not working properly
#     print(collection)

my_dictionary= {"A":1,"B":2,"C":3}  # this dictornary in reversed order working

for x in reversed(my_dictionary):
    print(x)
for key,value in my_dictionary.items():
    print(f"{key}={value}")

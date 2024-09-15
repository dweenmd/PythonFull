# collection = single variable to use multiple values
#List =[] ordered and changable .Duplicate ok  
#set ={} unordred an immutable, but add/remove ok . No duplicate
#Tupples=() ordered and unchangable , Duplicate ok faster

fruits= ["apple", "orange", "banana","coconat"]
print(fruits[::-1])

#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("apple" in fruits)

#add something with append
fruits.append("Pineapple")
for fruit in fruits:
    print(fruit)
#reassign values in list 
 
# fruits[0]="Mango"
# for fruit in fruits:
#     print(fruit)
# fruits.remove("apple")
# fruits.insert(0,pineapple)
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# pritn(fruits.index("apple"))
print(fruits.count("banana"))
print(fruits)

#  set ...   set like a list but ______ no dupicate

setfruits={"apple","banana", "apple", "pineapple", "mango", "cherry"}
print(setfruits)
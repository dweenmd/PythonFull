#dictionary = a collection of {key: value} pairs ordered and changable
#            no duplicates

capitals ={"USA":"Washintong D.C",
           "India": " new delhi",
           "China": "Beijing",
           "Russia":"Moscow"}
# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("USA"))

if capitals.get("japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist.")
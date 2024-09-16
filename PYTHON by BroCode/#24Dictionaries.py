# dictionary = a collection of {key: value} pairs, ordered and changeable
#              No duplicate keys allowed in a dictionary

# Creating a dictionary with country names as keys and their capitals as values
capitals = {
    "USA": "Washington D.C.", 
    "India": "New Delhi",      
    "China": "Beijing",        
    "Russia": "Moscow"         
}

# print(dir(capitals))                                        # This would print all the attributes and methods available for the dictionary object
# print(help(capitals))                                       # This provides detailed documentation of the dictionary and its methods

# Access the value associated with a key using the get() method
# print(capitals.get("USA"))                                    # This will print the capital of USA, which is "Washington D.C."

# Checking if a key exists in the dictionary using get()
# if capitals.get("japan"):                                 # get("japan") returns None because "Japan" is not a key in the dictionary
#     print("That capital exists")  
# else:
#     print("That capital doesn't exist.")                  # This message will be printed as "Japan" is not in the dictionary

# Updating the dictionary by adding a new key-value pair
# capitals.update({"Germany": "Berlin"})                    # Adds the key "Germany" with the value "Berlin" to the dictionary
# print(capitals)                                            # Prints the updated dictionary, now including "Germany": "Berlin"

# Removing an item from the dictionary using pop()
# capitals.pop("China")                        # Removes the key "China" and its associated value "Beijing"
# print(capitals)                              # Prints the dictionary after "China" is removed

# Removing the last inserted key-value pair using popitem()
# capitals.popitem()                          # Removes the last inserted key-value pair (depending on insertion order, this might be "Russia")
# print(capitals)                             # Prints the dictionary after the last item is removed

# Clearing all items from the dictionary using clear()
# capitals.clear()                           # Removes all key-value pairs from the dictionary, making it empty
# print(capitals)                            # Prints an empty dictionary

# Retrieving only the keys from the dictionary using keys()
# keys = capitals.keys()                     # The keys() method returns a view object of the dictionary's keys
# print(keys)                               # Prints all the keys in the dictionary (e.g., "USA", "India", etc.)

# Retrieving only the values from the dictionary using values()
# values = capitals.values()                # The values() method returns a view object of all the values in the dictionary
# print(values)                             # Prints all the values (e.g., "Washington D.C.", "New Delhi", etc.)

# Retrieving key-value pairs as tuples using items() and iterating over the dictionary
items = capitals.items()                    # The items() method returns a view object of key-value pairs as tuples

# Iterating through the dictionary and printing each key-value pair
for key, value in capitals.items():
    print(f" {key}: {value}")  # For each key-value pair, print the key (country) and the value (capital)

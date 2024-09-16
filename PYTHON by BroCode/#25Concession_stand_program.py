menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

cart = []
total = 0

# Display Menu
print("--------- Menu ---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")  # Formatting price to 2 decimal places
print("------------------------")

# Main loop
while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        print(f"{food.capitalize()} added to cart.")
    else:
        print("Sorry, that item is not on the menu. Please select again.")

# Display order and total
print("\n------ YOUR ORDER ------")
for food in cart:
    total += menu.get(food)
    print(f"{food.capitalize()}: ${menu.get(food):.2f}")
print("------------------------")
print(f"Total: ${total:.2f}")

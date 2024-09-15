print("Here are some items of food and groceries. Choose your items...")

# List of foods with prices
Foods = ["1. Pizza = $5.66", "2. Hotdog = $3.50", "3. Beef burger = $4.00", "4. Nachos = $1.50"]
showitem = ["Pizza", "Hotdog", "Beef burger", "Nachos"]
price = [5.66, 3.50, 4.00, 1.50]

# Print available items
print("\n".join(Foods))

# Shopping cart and total amount
cart = []
total = 0.0

# Infinite loop for user to select items
while True:
    item = input("Select Your Food (1-4) or quit by typing 'q': ")
    
    if item.lower() == 'q':
        break  # Exit the loop if user wants to quit
    
    # Check if input is a valid number between 1 and 4
    if item.isdigit() and 1 <= int(item) <= 4:
        item = int(item) - 1  # Convert to zero-based index
        quantity = int(input("Enter quantity: "))
        
        # Add selected item to cart and calculate total
        cart.append(f"{quantity}x {showitem[item]}")
        total += price[item] * quantity
        print(f"Added {quantity}x {showitem[item]} to your cart.\n")
    else:
        print("Invalid selection. Please choose a number between 1 and 4 or 'q' to quit.")

# Show final cart and total price
if cart:
    print("\nYour cart items:")
    print("\n".join(cart))
    print(f"Total price: ${total:.2f}")
else:
    print("Your cart is empty.")

import random

low = 1
high = 100

# Uncomment one of these to use
# number = random.randint(low, high)  # Random integer between low and high
# number = random.randint(1, 6)       # Random integer between 1 and 6 (simulating a die)
# number = random.random()            # Random float between 0 and 1

# Randomly choose between "rock", "paper", and "scissors"
options = ("rock", "paper", "scissors")
option = random.choice(options)

# Print the random choice
print(f"Randomly chosen option: {option}")

print()

# Shuffle and print a deck of cards
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
print("Shuffled cards:", cards)

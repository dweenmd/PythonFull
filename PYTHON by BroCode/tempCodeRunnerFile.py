import random

options = ("rock", "paper", "scissors")  # Corrected spelling of "scissors"
playerPoint = 0
computerPoint = 0

while True:
    player = input("Enter a choice (rock, paper, scissors): ").lower()
    computer = random.choice(options)

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    # No points for each player
    if (player == computer):
        playerPoint += 0
        computerPoint += 0

    # Points for player
    elif ((player == "rock" and computer == "scissors") or
          (player == "paper" and computer == "rock") or
          (player == "scissors" and computer == "paper")):
        playerPoint += 1

    # Points for computer
    else:
        computerPoint += 1

    print("------- Updated Points -------")
    print(f"Player Points:   {playerPoint}")  
    print(f"Computer Points: {computerPoint}")
    print("------------------------------")  

    if playerPoint == 10:
        print("----------- Result ------------")
        print("Player is the Winner!")
        print("-------------------------------")  
        check = input("Do you want to quit the game? (y/n): ").lower()
        if check == 'y':
            break
        else:
            playerPoint = 0
            computerPoint = 0

    if computerPoint == 10:
        print("----------- Result ------------")
        print("Computer is the Winner!")
        print("-------------------------------") 
        check = input("Do you want to quit the game? (y/n): ").lower()
        if check == 'y':
            break
        else:
            playerPoint = 0
            computerPoint = 0

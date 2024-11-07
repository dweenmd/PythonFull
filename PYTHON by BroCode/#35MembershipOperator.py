# membership operators= used to test whether a value of variable is found in a sequence
#                       (string,list,tuple, set or dictonary)
#                       1. in
#                       2. not in

word ="Apple"
letter= input("guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found.")


if letter not in word:
    print(f"{letter} was not found.") 
else:
    print(f"There is a {letter}")

#membership operator in dictionary
grades={"Sandy": "A",
        "Squidward": "B",
        "Spongebob":"C",
        "Patrick":"D"}
student = input("Enter the name of a student:")
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found.")
    
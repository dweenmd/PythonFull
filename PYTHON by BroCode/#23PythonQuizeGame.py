#python quize game
questions=("How many elements are in the preodic table? ",
            "Which animals lays in the largest eggs?",
            "What is the most abundent gass in the earth atmoaphare?",
            "How many bones are in the human body?",
            "Which plannet in the solar system is the hottest?")
options=(
        ("A. 116","B. 117","C. 118","D. 119"),
        ("A. Whale ","B. Ostrich ","C. Crocodile ","D. Elepahant"),
        ("A. Nitrogen ","B. Oxygen ","C. Carbon-Dioxide","D. Hydrogen"),
        ("A. 207", "B. 206","C.208","D. 209"),
        ("A. Mercury","B.Mars ","C. Earth ","D. Venus"))
answers=["C","B","A","B","D"]
guesses=[]
score=0
questions_num=0

for question in questions:
    print("_______________________")
    print (question)
    for option in options[questions_num]:
        print(option)
        
    guess=input("Enter (A/B/C/D): ").upper()
    guesses.append(guess)
    if guess==answers[questions_num]:
        print("CORRECT Answer.")
        score+=1
    else:
        print()
        print(f"Your ans is wrong .Correct answer is : {answers[questions_num]}")
    questions_num+=1

print("------------------------")
print("         RESULT         ")
print("------------------------")

print("answer:",end=" ")
for answer in answers:
    print(answer,end=" ")
print()
print("Guesses: ",end="")       
for guess in guesses:
    print(guess,end=" ")
print()
print(f"Score: {(score/len(questions))*100}%")
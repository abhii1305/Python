
import random

user_wins = 0
computer_wins= 0

options = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)

    computer_pick = options[random_number]
    print("computer picked",computer_pick + ".")

    if user_input == "rock"  and computer_pick == "scissors":
        print("You won!")
        user_wins+= 1
    elif user_input == "paper"  and computer_pick == "rock":
        print("You won!")
        user_wins+= 1
    elif user_input == "scissors"  and computer_pick == "paper":
        print("You won!")
        user_wins+= 1
    else:
        print("You Lost!")
        computer_wins+= 1


print("You won",user_wins,"times.")
print("Computer won",computer_wins,"times.")
print("Game-Over!!")



        
# import random

# print("~~~~~~~~Welcome to Rock Paper Scissors~~~~~~~~~~")
# user_score = 0
# comp_score = 0
# ties = 0

# name = input("Enter your name: ")
# print("""
#         Winning Rules
# 1. Paper vs Rock --> Paper
# 2. Rock vs Scissor --> Rock
# 3. Scissor vs paper --> Scissor """)
# while True:
#     print("""choices are:
#     1. Rock
#     2. Paper
#     3. Scissor""")
#     choice = int(input("Enter your choice from 1-3: "))
#     print()
    
#     while choice > 3 or choice < 1:
#         choice = int(input("Enter valid input: "))

#     if choice == 1:
#         user_choice = "Rock"
#     elif choice == 2:
#         user_choice = "Paper"
#     else:
#         user_choice = "Scissor"

#     print("The user's choice is", user_choice)
#     print("Now it's the computer's turn")

#     computer = random.randint(1, 3)

#     if computer == 1:
#         comp_choice = "Rock"
#     elif computer == 2:
#         comp_choice = "Paper"
#     else:
#         comp_choice = "Scissor"
#     print("The computer's choice is", comp_choice)

#     if (user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Paper"):
#         print("Paper wins")
#         result = "Paper"
#     elif (user_choice == "Scissor" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Scissor"):
#         print("Rock wins")
#         result = "Rock"
#     elif user_choice == comp_choice:
#         print("It's a Tie")
#         result = "Tie"
#     else:
#         print("Scissor wins")
#         result = "Scissor"

#     if result == "Tie":
#         ties += 1
#     elif result == user_choice:
#         print("User wins")
#         user_score += 1
#     else:
#         print("Computer wins")
#         comp_score += 1
        
#     print("Scores are:")
#     print(name, "'s score is", user_score)
#     print("Computer's score is", comp_score)
#     print("Ties are", ties)

#     repeat = input("Do you want to play again? (Yes/No): ")
#     if repeat.lower() == "no":
#         break
        
# print("Game over")


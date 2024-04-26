import random
def play_game():
    print("Welcome to 'Guess The Number' game")
    correct_number = random.randint(1,100)
    attempts = 0

    while True:
        guess = int(input("Enter any number between 1 to 100: "))
        attempts+=1

        if guess < correct_number:
            print("To Low , Try again!")
        elif guess > correct_number:
            print("To High , Try again!")
        else:
            print(f"Congratulations you guessed the number {correct_number} in {attempts} tries")
            break

play_game()


import random
lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number,highest_number)
guesses = 0
is_running = True

print("PYTHON GUESS RANDOM GAME")
print(f"Select a number between {lowest_number} and {highest_number}")

while is_running:
    guess = input("Guess a number: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_number or guess > highest_number:
            print("That guess is out of the range")
            print(f"Please Select a number between {lowest_number} and {highest_number}")
        elif guess>answer:
            print("number is too high")
        elif guess < answer:
            print("number is too low")
        else:
            print("number is correct")
            print(f"You guessed the number in {guesses} guesses")
            is_running = False
    else:
        print("INVALID INPUT")
        print(f"Please Select a number between {lowest_number} and {highest_number}")

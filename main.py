# Python Number Guessing Game
import random
lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number, highest_number)

guesses = 0
is_running = True 

print("Python Number Guessing Game")
print(f"Guess a number between {lowest_number} and {highest_number}")

while is_running:

    guess = input("Enter your guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1 

        if guess < lowest_number or guess > highest_number:
            print("The number is out of the guessing range")
            print(f"Please Select a Number Between {lowest_number} and {highest_number}") 
        elif guess < answer:
             print("Too Low! Try Again!")
        elif guess > answer:
            print("Too High! Try Again!")
        else:
            print(f"Congratulations! The number was {answer}")
            print(f"Number of Guesses: {guesses}")
            is_running = False
    else:  
        print("Invalid Guess")
        print(f"Please Select a Number Between {lowest_number} and {highest_number}")   
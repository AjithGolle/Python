# number guessing game with random function

import random 

low = 1
high = 100
ans = random.randint(low,high)
guesses = 0
is_running = True

print("****PYTHON GUESSING GAME****")
print(f"select a number between {low} and {high} :")

while is_running :
    guess = input("enter your guess:")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < low or guess > high :
            print("guess is outoff range!")
            print(f"please select a number between {low} and {high} :")
        elif guess < ans :
            print("too low Try again!")
        elif guess > ans :
            print("too high try again!")
        else :
            print(f"CORRECT! the answer was {ans}")
            print(f"number of guesses :{guesses}")
    else:
        print("Invalid Guess")
        print(f"please select a number between {low} and {high} :")
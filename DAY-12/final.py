#Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo
import random
print(logo)
# Allow the player to submit a guess for a number between 1 and 100.
guessed_number = random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
attempts=0
if difficulty == "easy":
  attempts =10
  
  print("You have 10 attempts remaining to guess the number.")

elif difficulty == "hard":
  attempts =5
  print("You have 5 attempts remaining to guess the number.")

print(guessed_number)
while True:
  users_guess = int(input("Make a guess: "))
  if users_guess > guessed_number:
    print("Too high.\nGuess again.")
    attempts -=1
    print(f"You have {attempts} attempts remaining to guess the number.")
    if attempts == 0:
      print("You've run out of guesses, you lose.")
      break
  elif users_guess < guessed_number:
    print("Too low.\nGuess again.")
    attempts -=1
    print(f"You have {attempts} attempts remaining to guess the number.")
    if attempts == 0:
      print("You've run out of guesses, you lose.")
      break
  elif guessed_number == users_guess:
    print(f"You got it! The answer was {guessed_number}.")
    break
  else:
    print("You entered an invalid input.")
    break

  


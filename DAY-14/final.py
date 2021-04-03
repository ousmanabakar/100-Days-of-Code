from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(account):
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(users_guess, account_a,account_b):
  if account_a["follower_count"] > account_b["follower_count"]:
    return users_guess =="a"
  else:
    return users_guess =="b"

print(logo)
score=0
account_b = random.choice(data) #1
while True:
  account_a = account_b #1
  account_b = random.choice(data)#2
  while account_a == account_b:
    account_b = random.choise(data)

  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Againts B: {format_data(account_b)}.")

  users_guess = input("Who has more followers? Type 'A' or 'B':").lower()
  is_correct = check_answer(users_guess, account_a, account_b)
  clear()
  print(logo)
  
  if is_correct:
    score +=1
    print(f"You're right! Current score: {score}.")
  else:
    print(f"Sorry that is wrong. Fianl score: {score}")
    break

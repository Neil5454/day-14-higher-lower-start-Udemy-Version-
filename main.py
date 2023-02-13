from art import logo, vs
from game_data import data
import random
from replit import clear


def format_data(account):
  """Takes the account data and returns the printable format."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return (f"{account_name}, {account_descr}, {account_country}.")

def check_answer(guess, a_follower_account, b_follower_account):
  """Take the user guess and and follower counts and returns if they got it right."""
  if a_follower_account > b_follower_account:
    return guess == "a" 
    """when guess is evaluated as being equal to "a", it will return True, otherwise False. Same as writing:
    if a_followers > b_followers:
      if guess = "a":
        return = True
      else:
        return False"""
  else:
    return guess == "b" # if b_followers greater than b_followers and guess=b, return True; otherwise fale

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Compare B: {format_data(account_b)}")
  guess = input("Who has more followers?  Type 'A' or 'B'").lower()
  
  a_follower_account = account_a["follower_count"]
  b_follower_account = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_account, b_follower_account)
  clear()
  print(logo)
  if is_correct:
    score += 1
    print(f"You're right!  Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong.  Final score: {score}.")
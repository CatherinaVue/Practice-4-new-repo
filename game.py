import random

print("Welcome to Rock-Paper-Scissors!")

def computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

Player_choice = input("Choose rock, paper, or scissors: ").lower().strip()

if Player_choice not in ["rock", "paper", "scissors"]:
    print("Invalid input. Please enter rock, paper, or scissors.")
else:
    print(f"You chose: {Player_choice}")
    print("Computer chooses:", computer_choice())

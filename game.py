import random

def computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

if __name__ == "__main__":
    print("Computer chooses:", computer_choice())
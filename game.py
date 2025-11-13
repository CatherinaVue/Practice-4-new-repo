print("Welcome to Rock-Paper-Scissors!")

Player_choice = input("Choose rock, paper, or scissors: ").lower().strip()
if Player_choice not in ["rock", "paper", "scissors"]:
    print("Invalid input. Please enter rock, paper, or scissors.")
else:
    print(f"You chose: {Player_choice}")
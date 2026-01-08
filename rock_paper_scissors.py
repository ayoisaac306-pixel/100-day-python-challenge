import random

game = ["rock", "paper", "scissors"]

computer = random.choice(game)

user = input("Enter your choice (Rock, Paper, Scissors): ").lower()

if user == computer:
    print(f"Computer chose {computer}. It's a tie!")
elif user == "rock" and computer == "scissors":
    print(f"Computer chose {computer}. You win!")
elif user == "paper" and computer == "rock":
    print(f"Computer chose {computer}. You win!")
elif user == "scissors" and computer == "paper":
    print(f"Computer chose {computer}. You win!")
elif user == "paper" and computer == "scissors":
    print(f"Computer chose {computer}. You lose!")
elif user == "scissors" and computer == "paper":
    print(f"Computer chose {computer}. You win!")
elif user == "scissors" and computer == "rock":
    print(f"Computer chose {computer}. You lose!")
elif user == "paper" and computer == "rock":
    print(f"Computer chose {computer}. You lose!")
elif user == "rock" and computer == "paper":
    print(f"Computer chose {computer}. You lose!")
else:
    print("Enter valid choice")
import random

while True:
    dice = input("Roll dice: ").lower()
    if dice == "roll":
        print(f"You rolled a {random.randint(1, 6)}")
    else:
        print("Enter(roll to play)")      

    roll_again = input("Roll again?: ").lower()
    if roll_again == "roll":
            print(f"You rolled a {random.randint(1, 6)}")
    elif roll_again == "no":
            print("Game over")
            break
    else:
        print("Enter (roll/no)")
    
                     
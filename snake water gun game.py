import random

while True:
        computer = random.choice(["snake", "water", "gun"])

        
        while True:
                  choice = input("Enter (snake/water/gun): ").lower()
                  if choice in ["snake", "water", "gun"]:
                       break
                  print("Please enter valid option")  


        if choice == computer:
            print(f"computer chose {computer}")
            print("Draw!")
        elif choice == "snake" and computer == "water":
            print(f"computer chose {computer}")    
            print("Congratulations you won!")
        elif choice == "water" and computer == "gun":
            print(f"computer chose {computer}")    
            print("Congratulations you won!")
        elif choice == "gun" and computer == "snake":
            print(f"computer chose {computer}")    
            print("Congratulations you won!")
        else:
            print(f"computer chose {computer}")    
            print("You lose, try again!")


        play_again = input("Do you want to play again?(y/n): ").lower()

        if play_again == "y":
            continue
        elif play_again == "n":
            print("Goodbye")
            break
        else:
             print("Enter y/n")    



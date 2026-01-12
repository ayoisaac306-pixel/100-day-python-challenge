import random

computer = random.randint(1, 10)


try:
    user = int(input("Enter a number from [1-10]: "))
except ValueError:
    print("Enter a valid number")    

print(f"Computer choice was: {computer}")

if user == computer:
    print("You won!")
else:
    print("Oops try again")        
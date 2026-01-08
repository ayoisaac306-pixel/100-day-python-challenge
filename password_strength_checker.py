import string

def password_strength_checker(password):
    strength = 0

    if len(password) >= 8:
      strength += 1
    if any(char.islower() for char in password):
       strength += 1
    if any(char.isupper() for char in password):
       strength += 1
    if any(char.isdigit() for char in password):
       strength += 1
    if any(char in string.punctuation for char in password):
       strength += 1  

    if strength == 5:
       return "Very strong"
    elif strength == 4:
       return "Strong"
    elif strength == 3:
       return "Medium"
    elif strength == 2:
       return "Weak"
    else:
       return "Very weak"      

password = input("Enter password")

print("password strength:", password_strength_checker(password))
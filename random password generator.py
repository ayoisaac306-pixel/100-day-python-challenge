import secrets
import string

def generate_password(length, use_lower, use_upper, use_digits, use_symbols):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{}<>?/"

    pool = ""
    if use_lower: pool += lowercase
    if use_upper: pool += uppercase
    if use_digits: pool += digits
    if use_symbols: pool += symbols

    if not pool:
        raise ValueError("Select at least one character type!")

    password_chars = []
    if use_lower: password_chars.append(secrets.choice(lowercase))
    if use_upper: password_chars.append(secrets.choice(uppercase))
    if use_digits: password_chars.append(secrets.choice(digits))
    if use_symbols: password_chars.append(secrets.choice(symbols)) 

    while len(password_chars) < length:
        password_chars.append(secrets.choice(pool))

    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

print("\n===== ADVANCE PASSWORD GENERATOR (CLI)")
print("----------------------------------------")

try:
    length = int(input("Enter password length: "))

    print("\nSelect character types:")
    use_lower = input("Include lowercase (y/n): ").lower() == "y"
    use_upper = input("Include uppercase (y/n): ").lower() == "y"
    use_digits = input("Include digits (y/n): ").lower() == "y"
    use_symbols = input("Include symbols (y/n): ").lower() == "y"

    password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
    print("\n✅ Your generated password:")
    print(password)

except ValueError as e:
    print(f"Error: {e}")
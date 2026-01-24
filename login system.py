FILE_NAME = "users.txt"

def register():
    username = input("Choose a username: ").strip()
    password = input("Choose a password: ").strip()


    try:
        with open(FILE_NAME, 'r') as file:
            for line in file:
                saved_user, saved_pass = line.strip().split(":")
                if saved_user == username:
                    print("Username already exist. Try another one.")
                    return
    except FileNotFoundError:
        pass
    #  Save new user
    with open(FILE_NAME, 'a') as file:
        file.write(f"{username}:{password}\n")

    print("Registration successful!")   


def login():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    try:
        with open(FILE_NAME, 'r') as file:
            for line in file:
                saved_user, saved_pass = line.strip().split(":")
                if  saved_user == username and saved_pass == password:
                    print("Login successful")
                    return
                print("Invalid username or password")
    except FileNotFoundError:
        print("No user registered yet. Register first!")


while True:
    print("1.Register")
    print("2.Login")
    print("3.Exit")

    choice = int(input("Choose an option (1-3): "))

    if choice == 1:
        register()
    elif choice == 2:
        login()
    elif choice == 3:
        print("Goodbye")
        break
    else:
        print("Invalid option")
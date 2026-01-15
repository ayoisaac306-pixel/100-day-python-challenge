while True:
    email = input("Enter email address: ").strip()
    if "@" not in email or email.count("@") != 1:
        print("Enter valid email address")
    elif "." not in email:
        print("Enter valid email address")    
    else:
        username, domain = email.split("@")
        print(f"Username: {username}")
        print(f"Domain: {domain}")
        break

        
    




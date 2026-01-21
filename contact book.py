contact_list = {}

def show_menu():
    print("\n----CONTACT BOOK----")
    print("1 Add contact")
    print("2 View contact")
    print("3 Update contact")
    print("4 Delete contact")
    print("5 Exit")

while True:
    show_menu()
    choise = input("Choose an option (1-5): ")

    if choise == "1":
        name = input("Enter name: ")
        phone = input("Enter phone no: ")
        email = input("Enter email: ")
        contact_list[name] = {"phone": phone, "email": email}
        print("Contact added successfully")
    elif choise == "2":
        name = input("Enter name to view contact: ")
        contact = contact_list.get(name)
        if contact:
            print(f"Name: {name}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
        else:
            print("Contact not found") 
    elif choise == "3":
        name = input("Enter name to update contact: ")
        if name in contact_list:
            phone = input("Enter new phone no: ")
            email = input("Enter new email: ")
            contact_list[name] = {"phone": phone, "email": email}
            print("Contact updated successfully")
        else:
            print("Contact not found")        
    elif choise == "4":
        name = input("Enter name to delete contact: ")
        if name in contact_list:
            contact_list.pop(name)
            print("Contact deleted successfully")
        else:
            print("Contact not found")
    elif choise == "5":
        print("Goodbye!")
        break
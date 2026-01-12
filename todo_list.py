todo_list = []

def show_menu():
    print("\n ---TO-DO LIST---")
    print("1 View tast")
    print("2 Add task")
    print("3 Delete task")
    print("4 Exit")

while True:
    show_menu() 
    choice = input("Choose an option [1-4]: ")   

    if choice == "1":
        if not todo_list:
            print("Your to-do list is empty")
        else:
            print("\n Your task")
            for index, task in enumerate(todo_list, start = 1):
                print(f"{index}.{task}")   
    elif choice == "2":
        task = input("Enter task")
        todo_list.append(task)
        print("Task added!")
    elif choice == "3":
        if not todo_list:
            print("No task to delete")
        else:
            try:
                num = int(input("Enter task number to delete"))
                if 1 <= num <= len(todo_list):
                    removed = todo_list.pop(num - 1)
                    print(f"Deleted: {removed}")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Enter a valid number")
    elif choice == "4":
        print("Goodbye")
        break 
    else:
        print("Enter valid option")

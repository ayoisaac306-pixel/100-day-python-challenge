import calendar

def display_month():
    year = int(input("Enter year (e.g 2026): "))
    month = int(input("Enter month (1-12): "))
    print("\nHere is the calender\n")
    print(calendar.month(year, month))

def display_year():
    year = int(input("Enter year (e.g 2026): "))
    print("\nHere is the calender\n")
    print(calendar.calendar(year))

while True:
    print("\n===== CALENDER APP =====")
    print("1. Show a month")
    print("2. Show a full year")
    print("3. Exit")

    option = input("Choose an option: ")

    if option == "1":
        display_month()
    elif option == "2":
        display_year()
    elif option == "3":
        print("Goodbye")
        break  
    else:
        print("Enter valid choice")          
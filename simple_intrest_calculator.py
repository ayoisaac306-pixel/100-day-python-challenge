def simple_intrest(p, r, t):
    return (p * r * t) / 100

def amount(p, r, t):
    return p + simple_intrest(p, r, t)

choice = input("What do you want to calculate? (SI/Amount)").lower()

if choice == "si":
    p = float(input("Enter principal: "))
    r = int(input("Enter rate: "))
    t = int(input("Enter time in years: "))
    result = simple_intrest(p, r, t)
    print(f"Simple intrest: {result}")
elif choice == "amount":
    p = float(input("Enter principal: "))
    r = int(input("Enter rate: "))
    t = int(input("Enter time in years: "))
    result = amount(p, r, t)
    print(f"Amount: {result}")
else:
    print(f"Invalid choice. Please type SI/Amount.")        
    


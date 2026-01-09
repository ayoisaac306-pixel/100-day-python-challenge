def multiplication_table(num):
    print(f"Multiplication table for {num}")
    for i in range (1, 13):
        print(f"{num} x {i} = {num * i}")

number = int(input("Enter number"))
print(multiplication_table(number))        
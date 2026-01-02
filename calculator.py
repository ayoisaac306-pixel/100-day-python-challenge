def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def square(a):
    return a * a

def cube(a):
    return a * a * a


# finding prime 
def primeNo(a):
    if a <= 1:
        return False
    for i in range(2, int(a**0.5)+ 1):
        if a % i == 0:
            return False
    return True    


number = int(input("Enter a number"))

if primeNo(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime")    



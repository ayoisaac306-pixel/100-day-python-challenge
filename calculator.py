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
        return f"{a} is not a prime number"
    for i in range(2, int(a**0.5)+ 1):
        if a % i == 0:
            return f"{a} is not a prime number"
    return f"{a} is a prime number"  


# odds and even checker for a number
def odd_even(a):
    if a % 2 == 0:
        return f"{a} is even number"
    else:
        return f"{a} is odd number"


# function for even odds checker
def even_odd(numbers):
    evens = [n for n in numbers if n % 2 == 0]
    odds = [n for n in numbers if n % 2 != 0]
    return evens, odds




            


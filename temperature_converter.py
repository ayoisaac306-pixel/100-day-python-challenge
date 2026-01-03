# celcius to fahrenheit
def c_to_f(c):
    return (c * 9/5) + 32

# fehrenheit to celcius
def f_to_c(f):
    return (f - 32) * 5/9

# celcius to kelvin
def c_to_k(c):
    return c + 273.15

# kelvin to celcius
def k_to_c(k):
    return k - 273.15

# fahrenheit to kelvin
def f_to_k(f):
    return (f - 32) * 5/9 + 273.15

# kelvin to fahrenheit
def k_to_f(k):
    return (k - 273.15) * 9/5 + 32

temp = float(input("Enter temperature: "))
from_unit = input("Convert from(C/F/K): ").upper()
to_unit = input("Convert to(C/F/K): ").upper()

# if/else console
if from_unit == "C" and to_unit == "F":
    result = c_to_f(temp)
elif from_unit == "F" and to_unit == "C":
    result = f_to_c(temp)
elif from_unit == "C" and to_unit == "K":
    result = c_to_k(temp)
elif from_unit == "K" and to_unit == "C":
    result = k_to_c(temp)
elif from_unit == "F" and to_unit == "K":
    result = f_to_k(temp)
elif from_unit == "K" and to_unit == "F":
    result = k_to_f(temp)
else:
    result = temp

# result
print(f"{temp}°{from_unit} = {result:.2f}°{to_unit}")

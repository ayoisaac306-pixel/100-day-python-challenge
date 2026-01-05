def calculate_bmi(weight, height):
    return weight / (height * height)

weight = float(input("Enter your weight (KG): "))
height = float(input("Enter your weight (M): "))

bmi = calculate_bmi(weight, height)

print(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
elif bmi > 30:
    print("Obese")
else:
    print("Enter valid (Height/Weight)")                
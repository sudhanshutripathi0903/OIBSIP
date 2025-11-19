weight = float(input("Weight in kg: "))
height = float(input("Height in meters: "))
bmi = weight / (height * height)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print("Your BMI:", bmi)
print("Category:", category)

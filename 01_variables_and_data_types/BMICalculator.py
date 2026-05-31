# BMI Calculator
# Read a person's weight in kilograms and height in metres. 
# Calculate their BMI and print the corresponding category — Underweight, Normal, Overweight, or Obese.

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in metres: "))
# Calculate BMI
bmi = weight / (height ** 2)
# Determine BMI category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"
print(f"Your BMI is: {bmi:.2f}. You are categorized as: {category}.")
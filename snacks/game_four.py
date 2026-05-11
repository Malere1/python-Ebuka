# Step 1: Start
# Step 2: Ask the user to enter weight in kilograms
# Step 3: Ask the user to enter height in meters
# Step 4: Calculate BMI using:
#         bmi = weight / (height * height)
# Step 5: Check BMI category
# Step 6: If BMI is less than 18.5, print "Underweight"
# Step 7: Else if BMI is between 18.5 and 24.9, print "Normal"
# Step 8: Else if BMI is between 25 and 29.9, print "Overweight"
# Step 9: Else, print "Obese"
# Step 10: End

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (meters): "))

bmi = weight / (height * height)

print("BMI =", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")

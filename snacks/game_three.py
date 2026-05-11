# Step 1: Start
# Step 2: Ask the user to enter age
# Step 3: Check if age is under 5
# Step 4: If true, price is "Free"
# Step 5: Else check if age is between 5 and 12
# Step 6: If true, price is "$5"
# Step 7: Else check if age is between 13 and 64
# Step 8: If true, price is "$12"
# Step 9: Otherwise, price is "$8"
# Step 10: Print the price
# Step 11: End

age = int(input("Enter your age: "))

if age < 5:
    print("Price = Free")
elif age <= 12:
    print("Price = #5")
elif age <= 64:
    print("Price = #12")
else:
    print("Price = #8")

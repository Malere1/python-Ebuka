# Step 1: Start
# Step 2: Ask the user to enter first integer (x)
# Step 3: Ask the user to enter second integer (y)
# Step 4: Check if y is equal to 0
# Step 5: If y is 0, print "Cannot divide by zero"
# Step 6: Otherwise, divide x by y
# Step 7: Print the result
# Step 8: End

x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))

if y == 0:
    print("Cannot divide by zero")
else:
    result = x / y
    print("Result =", result)

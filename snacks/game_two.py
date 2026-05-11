# Step 1: Start
# Step 2: Ask the user to enter three integers (a, b, c)
# Step 3: Assume the first number (a) is the largest
# Step 4: Check if b is greater than the current largest
# Step 5: If true, make b the largest
# Step 6: Check if c is greater than the current largest
# Step 7: If true, make c the largest
# Step 8: Print the largest number
# Step 9: End

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print("Largest =", largest)

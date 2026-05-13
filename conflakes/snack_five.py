#write a Python program to create the multiplication table (from 1 to 10) of a g
... iven number. Sample input: 6 Expected Output:
print("Multiplication Table:")
print("  ×", end=" ")
for i in range(1, 11):
    print(f"{i:2}", end=" | ")
print()

# Print each row of the table
for i in range(1, 11):
    print(f"{num} × {i:2} = {num * i:4}", end=" | ")
    if i < 9:
        print()
    else:
        print()


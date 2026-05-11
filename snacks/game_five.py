#Discount Eligibility :  Ask for total_bill and is_member ("yes" or "no"). Apply discount: ● If total_bill >= 1000 and is_member == "yes" #→ 10% off ● If total_bill >= 1000 but not member → 5% off ● Else → No discount Print final amount and discount message.

# Step 1: Start
# Step 2: Ask the user to enter total bill
# Step 3: Ask the user if they are a member ("yes" or "no")
# Step 4: Check if total bill is greater than or equal to 1000
# Step 5: If yes and member is "yes", apply 10% discount
# Step 6: Else if total bill is greater than or equal to 1000
#         and member is "no", apply 5% discount
# Step 7: Else, apply no discount
# Step 8: Calculate final amount
# Step 9: Print discount message
# Step 10: Print final amount
# Step 11: End

total_bill = float(input("Enter total bill: "))
is_member = input("Are you a member? (yes/no): ")

if total_bill >= 1000 and is_member == "yes":
    discount = total_bill * 0.10
    final_amount = total_bill - discount
    print("10% discount applied")
elif total_bill >= 1000:
    discount = total_bill * 0.05
    final_amount = total_bill - discount
    print("5% discount applied")
else:
    discount = 0
    final_amount = total_bill
    print("No discount")

print("Final amount =", final_amount)           


def apply_discount(item_name, original_price, promo_code):
    if original_price < 0:
        return "Price cannot be negative"

    if promo_code == "SAVE10":
        discounted_price = original_price * 0.90

    elif promo_code == "HALFOFF":
        discounted_price = original_price * 0.50

    else:
        discounted_price = original_price

    return discounted_price

print("Test 1")
print(apply_discount("Laptop", 1000, "SAVE10"))

print("\nTest 2")
print(apply_discount("Phone", 800, "HALFOFF"))

print("\nTest 3")
print(apply_discount("Keyboard", 200, "INVALID"))

print("\nTest 4")
print(apply_discount("Mouse", 150, ""))

print("\nTest 5")
print(apply_discount("Book", 0, "SAVE10"))

print("\nTest 6")
print(apply_discount("Tablet", -500, "SAVE10"))
# Expected Output: Price cannot be negative

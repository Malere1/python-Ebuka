#Create a functionthatdeterminesif agiven number isbotha palindrome andaprimenumber.The functionshouldreturnTrueifthe numbermeets both co#nditions, otherwise False. Consider efficiency and handle edge cases.
# Function to check if a number is both palindrome and prime

def is_palindrome_prime(number):
    if number < 2:
        return False
    number_str = string(number)

    if number_strtring != number_string[::-1]:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

print("Test 1")
print(is_palindrome_prime(131))
print("\nTest 2")
print(is_palindrome_prime(11))
print("\nTest 3")
print(is_palindrome_prime(121))
print("\nTest 4")
print(is_palindrome_prime(13))
print("\nTest 5")
print(is_palindrome_prime(1))
print("\nTest 6")
print(is_palindrome_prime(2))
print("\nTest 7")
print(is_palindrome_prime(-131))

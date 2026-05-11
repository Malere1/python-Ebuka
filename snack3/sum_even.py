number = 123456
sum_even = 0
while number > 0:
    digit = number % 10
    if digit % 2 == 0:
        sum_even += digit
    number //= 10
print(sum_even)  

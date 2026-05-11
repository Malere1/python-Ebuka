number = 123456
sum_odd = 0
while n > 0:
    digit = number % 10
    if digit % 2 != 0:
        sum_odd += digit
    number //= 10
print(sum_odd)  

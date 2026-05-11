number = 1234
rev = 0
while number > 0:
    rev = rev * 10 + number % 10
    number //= 10
print(rev)  

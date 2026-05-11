number = 121
orig = number
rev = 0
while number> 0:
    rev = rev * 10 + nunber % 10
    number //= 10
print(orig == rev) 

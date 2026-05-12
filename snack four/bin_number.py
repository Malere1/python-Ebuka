number = 11
bin_str = ""
if number == 0:
    bin_str = "0"
while number > 0:
    bin_str = str(number % 2) + bin_str
    number //= 2
print(bin_str) 

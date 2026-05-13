# Write a program that calculate sum of multiple of 10 between 1 to 20_000.

total = 0

for i in range(1, 20001):

    if i % 10 == 0:
        total += i

print(total)

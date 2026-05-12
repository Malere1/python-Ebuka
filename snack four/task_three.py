pass_count = 0
fail_count = 0

for i in range(1, 16):

    score = int(input("Enter score: "))

    if score >= 45:
        pass_count += 1

    else:
        fail_count += 1

print("Passed students:", pass_count)
print("Failed students:", fail_count)

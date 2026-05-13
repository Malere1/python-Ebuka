##Write a python program that accept  scores of 15 student from teacher(user) and determine the number of students that pass or fail. pass mark is 45
pass_count = 0
fail_count = 0
for i in range(1,16):
score = float(input(f"Enter score for student {i}: "))
if score >= 45:
print(f"Student {i} has passed with a score of {score}.")
pass_count += 1
else:
print(f"Student {i} has failed with a score of {score}.")
fail_count += 1


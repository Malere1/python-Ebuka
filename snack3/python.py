string = "python"
vowels = "aeiouAEIOU"
for i, ch in enumerate(s):
    if ch in vowels:
        print(i)  
        break

letter = input("Enter one letter: ")

if len(letter) != 1 or not letter.isalpha():
    print("Invalid input")
else:
    letter = letter.lower() 
    if letter in "aeiou":
        print("Vowel")
    else:
        print("Consonant")

text= input("Enter a String:")
vowels = "aeiouAEIOU"
found_vowels = []

for i in text:
    if i in vowels:
        found_vowels.append(i)
print("Vowels in the string:", found_vowels)

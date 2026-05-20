text = input("Enter a string:")
#text = text.replace("", "").upper()
reversed_text = text[::-1]
if text == reversed_text:
    print("Palindrome")
else:
    print("Not")

print(reversed_text)

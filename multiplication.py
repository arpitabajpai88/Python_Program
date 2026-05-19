def multiplication(n):
    for i in range(1,11):
        mul = n * i
        print (f" {n} * {i} = {mul}")
s=int(input("Enter a num:"))
print(f"Table of {s} is")
multiplication(s)
leap = int(input("Enter a year:"))

if (leap % 4 == 0 and leap % 100 != 0) or (leap % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap year")


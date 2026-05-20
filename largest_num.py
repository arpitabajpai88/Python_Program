a = int(input("ENter a num:"))
b = int(input("ENter a num:"))
c = int(input("ENter a num:"))

if (a>=b and a>=c):
    print("Largest num is:",a)
elif(b>=a and b>=c):
    print("Largest num is:",b)
elif(c>=a and c>=b):
    print("Largest num is:",c)
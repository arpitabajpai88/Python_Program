def prime(n):

    if n <=1:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True 
s = int(input("Enter a num:"))
if prime(s):
    print("Prime")
else:
    print("Not Prime")

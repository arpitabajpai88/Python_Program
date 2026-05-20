x = [10,10,70,70,62,52,52,45,12,45]
#duplicate= set(x)   #using set
#print(duplicate)
#y= list(dict.fromkeys(x))  #use dict.fromkeys()
#print (y)
num = [] #use LOOP + Append method 

for i in x:
    if i not in num:
        num.append(i)
num.sort()  #ascending order
print(num)
num.sort(reverse=True) #descending order
print(num)

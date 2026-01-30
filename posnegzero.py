num=int(input("Enter a number"))

if(num==0):
    print(num, "is zero")
elif(num>0):
    print(num, "is positive")
else:
    print(num, "is negative")

a=2

print("a is greater" if a > 0 else "a is less")

from enum import nonmember

def fibbonacci_recursive(n):
    if n < 1:
        print("Input is Incorrect")
        return None
    elif n<2 :
        return n
    else:
        return fibbonacci_recursive(n-1)+fibbonacci_recursive(n-2)

num_terms=10
print("Fibbonacci sequence:")
for i in range(num_terms):
    print(fibbonacci_recursive(i),end="")
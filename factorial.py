def fact(n):
    if (n==1):
        return 1
    else:
        return n*fact(n-1)
num=int(input("Enter a number: "))
if isinstance(num,int) and num>0:
    print("Factorial: ",fact(num))
else:
    print("Cannot determine factorial.")
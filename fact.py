n=int(input("enter a number:"))
fact=1
if n<0:
    print("factorial does not exist for negative numbers")
elif n == 0:
    print("factorial of a is",1)
else:
 for i in range (1,n+1):
    fact=fact*1
    print("fact",n)



a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if(a>b):
    smaller=b
else:
    smaller=a
    GCD=1
    for i in range(1,smaller+1):
        if ( a % i == 0) &(b%i==0):
            GCD=i
    print(GCD)

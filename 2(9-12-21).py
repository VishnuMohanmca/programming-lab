n=int(input("Enter the number"))
a=0
b=1
print("Fibonacci SERIES:")
print(a)
print(b)
for i in range(0,n+1):
    fib=a+b
    print(fib)
    a=b
    b=fib
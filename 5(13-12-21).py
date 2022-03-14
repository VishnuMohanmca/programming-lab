n=int(input("Enter the number"))
factors=[]
for i in range(1,n+1):
    for j in range(1,i+1):
        if i*j==n:
            factors.append(i)
            factors.append(j)
print("factors of "+str(n)+" :")
for i in factors:
    print(i)
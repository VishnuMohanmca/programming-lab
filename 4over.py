n=int(input("enter a limit:"))
a=[]
for i in range(0,n):
  c=int(input("Enter a value:"))
  if c > 100:
   a.append("over")
  else:
   a.append(c)
print(a)
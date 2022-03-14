n=int(input("Enter the limit:"))
lst = []
print("Enter the values:")
for i in range(0,n):
  m=int(input())
  lst.append(m)
print("list is:",lst)
sum=0
for i in lst:
 sum=sum+i
print("sum of the given list is:",sum)


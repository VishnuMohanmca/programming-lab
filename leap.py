styr=int(input("enter a start year:"))
endyr=int(input("enter a end year:"))
lst=[]
for i in range(styr,endyr):
    if(i%4 == 0 and i%100!= 0)or i%400 == 0:
        lst.append(i)
print("leap year:",lst)



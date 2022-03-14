start_yr=int(input("Enter the starting year:"))
end_yr=int(input("Enter the end year:"))
lst=[]
for i in range(start_yr,end_yr):
    if((i%4==0 and i%100!=0) or i%400==0):
        lst.append(i)

print("leap year",lst)
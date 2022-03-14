start=int(input("Enter the intial range"))
end=int(input("Enter the End range"))
if(start<1000):
    print("enter a 4 dig num")
if(end<start):
    print("Enter a value greater than inital range")
    end = int(input("Enter the End range"))
print("Perfect squares and even numbers in the range"+str(start)+"-"+str(end)+":")
for i in range(start,end):
    if i%2==0 and i**(1/2)==int(i**(1/2)):
        print(i)
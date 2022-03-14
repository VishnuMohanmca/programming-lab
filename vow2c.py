element=str(input("Enter a string:"))
v=['a','e','i','o','u']
lst=[]
for i in element:
    if(i in v and i not in lst):
     lst.append(i)
print("vowels present in the string are:",lst)

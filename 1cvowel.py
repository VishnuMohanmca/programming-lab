ele=str(input("enter a string:"))
vowels=['a','e','i','o','u']
lst=[]
for x in ele:
    if(x in vowels and x not in lst):
        lst.append(x)
print("vowels present in the given statement:",lst)
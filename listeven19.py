list = [4,12,13,14,15,16,17,18,19,21,23,24,25]
listodd=[]
print("the orginal list is:",list)
for i in list:
    if i % 2!=0:
        listodd.append(i)
print("list after removing even number is:")
print(listodd)
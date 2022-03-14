lst=[1,2,9,-3,5,6,-8,7,-10,18,44]
for i in lst:
    if i <= 0:
        lst.remove(i)
print("positive list are:",lst)
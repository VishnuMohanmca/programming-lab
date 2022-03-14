list1 = [1, 5, 10, 11, -5, 12, 0, 8, -77, 76, -34, 99]
for num in list1:
       if num <= 0:
            list1.remove(num)
print("positive numbers are:",list1)

a = [3, 4, 6, 7, 9, 1]
b = [5, 6, 7, 8, 10, 12, 13]
c = sum(a)
print("sum of a:", c)
c = sum(b)
print("sum of b:", c)
if sum(a) <= sum(b) and sum(a) >= sum(b):
    print("Sums of a is equal to sum of b")
else:
    print("Sums of a is not equal to sum of b")

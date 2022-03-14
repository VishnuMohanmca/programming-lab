d = {'beena': 30, 'arjun': 4, 'fahad': 8, 'thimothy': 6, 'midhun':35}
l = list(d.items())
l.sort()
print('Ascending order is', l)

l = list(d.items())
l.sort(reverse=True)
print('Descending order is', l)

dict = dict(l)
print("Dictionary", dict)

# d = {'beena': 30, 'arjun': 4, 'fahad': 8, 'thimothy': 6, 'midhun':35}
# print('Ascending ordered name list : ',dict(sorted(d.items())))
# print('Decending ordered name list : ',dict(sorted(d.items(), reverse=True)))
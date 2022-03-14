dict1 = {'batsman': 4, 'bowler': 3, 'spinner':2, 'keeper':1}
dict2 = {'actor':3, 'actress': 2, 'director':1, 'makeupman': 1}
print("dictionary1:",dict1)
print("dictionary2:",dict2)
d=dict1.copy()
d.update(dict2)
print(d)


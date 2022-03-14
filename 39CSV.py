import csv

with open('sample.csv') as file:
    data = csv.reader(file)
    for row in data:
        print(row)

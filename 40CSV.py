import csv

with open("sample.csv") as file:
    d = csv.DictReader(file)
    print("sr.no   student name   division   roll no")
    print("-----------------------------------------")
    for i in d:
        print(i['sr.no'], i['student name'], i['division'], i['roll no'])

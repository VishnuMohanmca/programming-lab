file = open("demo.txt", "r")

#read content of file to string
data = file.read()

#get number of occurrences of the substring in the string
occurrences = data.count("")

print('Number of occurrences of the word :', occurrences)
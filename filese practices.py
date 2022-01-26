##p=open("file1.txt","a")
##with open("file1.txt","w")as f:
##    print(f.write("shivay"))
##    print(f.read())
##
from csv import reader
with open("file.csv","r")as f:
    csv_reader=reader(f)
for row in csv_reader:
    print(row)

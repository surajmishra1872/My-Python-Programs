name = input("enter your name")
age = int(input("enter your age"))
s=name.lower()
if age>=12 and s[0]=="a" or s[0]=="A":
    print("go")
else:
    print("no")
    

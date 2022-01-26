print("welcome to SKF circuse")
age =input(" please enter your age")
age = int(age)
if age==0 or age <0:
    print("you cant watch show")
elif 0<age<=3:
    print("ticket price: free")
elif 3<age<=12:
    print("ticket price:150")
elif 12<age<=60:
    print("ticket price:250")
else:
    print("ticket price:200")
    

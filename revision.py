##print("Suraj" ,end="kr.")
##print("mishra\n\n")
##print("Suraj","Mishra",sep="Kr.")
##print("\n")
##
##name="Suraj"
##age=20
##print(f"your name is \t{name} and age is\t{age}")
##print("Your Name is:"+name+"\tand Your age is:"+str(age))
##print("\n")
##
##
##var="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
##print(var[0:26:2])
##print(var.replace("A","AlphaBates\n"))
##print(name.center(len(name)+6,"*"))
##print("\n \n")


#if else
##while(True):
##    winnum=20
##    ynum=eval(input("enter your number:"))
##    if winnum==ynum:
##        print("Congratulation !! You guase correct number.")
##        break
##
##    else:
##        if(ynum<20):
##            print("You Number is below than 20.")
##        else:
##            print("Your Number is Greater than 20.")

##print("\n \n")

#ticket counter

##age=eval(input("Welcome to Ajanta Circuse\n Enter Your Age:"))
##if age==10:
##    print("Your Ticket Price is:10")
##elif age>15 and age<20:
##    print("Your Ticket Price is:30")
##elif age>=20 and age<50:
##    print("Your Ticket price is:50")
##elif 50<=age<80:
##    print("Your Ticket Price is:70")
##else:
##    print("Your Ticket Price is:40")

# Password Matching
##passwordlist=["1234","0532","2332","1873","1443","2212"]
##print("Welcome to Bank Of Baroda")
##password=input("Enter Your Password:")
##if password in passwordlist:
##    print("Password Matched")
##else:
##    print("Password not matched")

#print sum of any Number

##n=int(input("Enter Your Number:"))
##total=0
##for i in range(0,n+1):
##    total=total+i
##print(total)


#print any number table

#while loop

##n1=int(input("Enter Any Number:"))
##n2=int(input("Enter A number where till you want atble:"))
##total=0
##i=1
##while(i<=n2):
##    total=n1*i
##    print(n1,"*",i,'=',total)
##    i+=1


#for loop

##n1=int(input("Enter Any Number:"))
##n2=int(input("Enter A number where till you want A tble:"))
##for i in range(1,n2+1):
##    print(n1,'*',i,'=',n1*i)


#function Inside function

##def greter(a,b):
##    if(a>b):
##        return a
##    else:
##        return b
##def greatest(a,b,c):
##    bigger=greter(a,b)
##    return greter(bigger,c)
##print(greatest(1,2,3))


#word counter
##def word_counter(a):
##    dic={}
##    for i in a:
##        dic[i]=a.count(i)
##    return dic
##print(word_counter("jahaj hai"))

#convert a list in to dictonary
##A=[1,'a',2,'b',3,'c',4,'d']
# Python3 program to Convert a
# list to dictionary

##def Convert(lst):
##	res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
##	return res_dct
##		
### Driver code
##
##print(Convert(A))
##dic={}
##for i in range(0,len(A),2):
##    dic[A[i]]=A[i+1]
##print(dic)

#list dictionary set comprehnsions

##square=['even'  for i in range(1,11)  if i%2==0]
##print(square)
##odd_even=['even'if i%2==0 else 'odd' for i in range(1,11)]
##print(odd_even)

#dictionary comprehnsion
##dic={i:i**2 for i in range(1,11)}
##print(dic)
##dic={i:"even" if i%2==0 else 'odd' for i in range(1,11)}
##print(dic)

#*args and **kwargs

##def square(*args):
##    square=1
##    for i in args:
##        square*=i
##        print(square)
##num=[8,2,3,4,5,6]
##square(*num)

##a=("p"*2)*3
##b=("p"*3)*2
##print(a==b)

#enumerate function

##name=["Suraj","Kumar","Mishra"]
##for pos,value in enumerate(name):
##    print(f"{pos}------>{value}")

#zip function

##name=['suraj','kumar','mishra']
##print(list(zip(name)))

##l1=[1,2,3,4,5,6]
##l2=[7,8,9,10,11,12]
##l3=zip(l1,l2)
##l4=[]
##for i in l3:
##    avg=sum(i)/len(i)
##    l4.append(int(avg))
##print(l4)


#Unzip a list or tuples and many more

#l1=[1,2,3,4,5]
##l2=['a','b','c','d','e']
##l3=zip(l1,l2)
##print(list(l3))
##l3=[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
##num,alpha=zip(*l3)
##print(num)
##print(alpha)

#Advance min and max function

##student=[
##{"name":"Suraj","age":20,"score":86},
##{"name":"MishraG","age":21,"score":56}
##    ]
##print(max(student,key=lambda x:x.get("score"))["name"])


##a={"name":"MishraG","age":21,"score":56}
##print(a.get("name","Not Found"))

#pass function as argument

##def func2(func,l):
##    l1=[]
##    for i in l:
##        l1.append(func(i))
##    return l1
##def func1(a):
##    return a**2
##lis=[1,2,3,4,5]
##print(func2(func1,lis))

#raise error

##def add(a,b):
##    if(type(a)==int and type(b)==int):
##        return a+b
##    raise TypeError("Tumse na ho payega munna")
##print(add(1,"a"))

##while True:
##    try:
##        age=int(input("enter age:"))
##        
##    except:
##        print("You Enter Wrong data type.")
##        break
##    if age>18:
##        print("you can play this game")
##    else:
##        print("you can not play this game")

#Debuging
##import pdb
##pdb.set_trace()
##name=print("enter name:")
##age=print("age:")
##age2=age+5
##print(age2)
##print(name)

##
##def nums(n):
##    for i in range(1,n+1):
##        yield(i)
##print(nums(10))
##
##for i in nums(10):
##    print(i)

#decorator
##def decorator_function(func):
##    def wrapper_function():
##        print("This is awesome function.")
##        func()
##    return wrapper_function
##@decorator_function
##def func1():
##    print("This is function 1")
##def func2():
##    print("This is function 2")
##func1()m 
##func1=decorator_function(func1)
##func1()
##v=decorator_function(func1)
##v()

##def decorator_function(func):
##    def wrapper_function(*args):
##        print("This is amazing function")
##        func(*args)
##    return wrapper_function
##@decorator_function
##def add(*args):
##    print(sum(args))
##@decorator_function
##def abss(*args):
##    print(sum(args))
####
##add(4,2,4)
##abss(4,2,3)


#best programing fact

##from functools import wraps
##def decorator_function(func):
##    @wraps(func)
##    def wrapper_function(*args,**kwargs):
##        """This is doc string of wrapper function"""
##        print("this is amazing function.")
##        func(*args,**kwargs)
##    return wrapper_function
##@decorator_function
##def add(a,b):
##    """This is add function"""
##    print(a+b)
##    
##print(add.__doc__)

##def mygenerator():
##    print('First item')
##    yield 10
##
##    return
##
##    print('Second item')
##    yield 20
##
##    print('Last item')
##    yield 30
##gen = mygenerator() 
##print(next(gen))
##print(next(gen))

#magic of return
##def func():
##    print("Hello1")
##    return
##    print("Hello2")
##func()

##def nums(n):
##    for i in range(1,n+1):
##        yield(i)
##print(nums(10))
##
##for a in nums(10):
##    print(a)
##for b in nums(10):
##    print(b)
##
##square=(i**2 for i in range(1,11))
##print(square)
##for i in square:
##    print(i)
##for j in square:
##    print(j)



#Object Oriented programming


##class student:
##    def __init__(self,name,branch):
##        self.names=name
##        self.branch=branch
##obj1=student("Suraj","IT")
##print(obj1.names)
##print("Your name is"+obj1.names+"Branch is"+obj1.branch)
##print(f"Your name is:{obj1.names} and Branch is:{obj1.branch}")


#Tkinter Music Player

##import pygame
##from pygame import mixer
##from tkinter import *
##import os
##
##def playsong():
##    currentsong=playlist.get(ACTIVE)
##    print(currentsong)
##    mixer.music.load(currentsong)
##    songstatus.set("Playing")
##    mixer.music.play()
##
##def pausesong():
##    songstatus.set("Paused")
##    mixer.music.pause()
##
##def stopsong():
##    songstatus.set("Stopped")
##    mixer.music.stop()
##
##def resumesong():
##    songstatus.set("Resuming")
##    mixer.music.unpause()    
##
##root=Tk()
##root.title('ProjectGurukul Music player project')
##
##mixer.init()
##songstatus=StringVar()
##songstatus.set("choosing")
##
###playlist---------------
##
##playlist=Listbox(root,selectmode=SINGLE,bg="DodgerBlue2",fg="white",font=('arial',15),width=40)
##playlist.grid(columnspan=5)
##
##os.chdir(r'E:\SONGS')
##songs=os.listdir()
##for s in songs:
##    playlist.insert(END,s)
##
##playbtn=Button(root,text="play",command=playsong)
##playbtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
##playbtn.grid(row=1,column=0)
##
##pausebtn=Button(root,text="Pause",command=pausesong)
##pausebtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
##pausebtn.grid(row=1,column=1)
##
##stopbtn=Button(root,text="Stop",command=stopsong)
##stopbtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
##stopbtn.grid(row=1,column=2)
##
##Resumebtn=Button(root,text="Resume",command=resumesong)
##Resumebtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
##Resumebtn.grid(row=1,column=3)
##
##mainloop()


#instance method


##class student:
##    def __init__(self,fname,lname,rollnum):
##        self.fname=fname
##        self.lname=lname
##        self.rollnum=rollnum
##    def fulldetail(self):
##        return (f"Full name is:{self.fname+self.lname} & Roll Number  is:{self.rollnum}")
##obj=student("Suraj","Mishra",42)
##print(obj.fname)
##print(obj.lname)
##print(obj.rollnum)
##print(obj.fulldetail())

##class student:
##    def __init__(self,fname,lname,rollnum):
##        self.fname=fname
##        self.lname=lname
##        self.rollnum=rollnum
##    def fulldetail(self,collage):
##        #self.collage=collage
##        return (f"Full name is:{self.fname+self.lname} & Roll Number  is:{self.rollnum} - collage name is:{collage}")
##obj=student("Suraj","Mishra",42)
##print(obj.fname)
##print(obj.lname)
##print(obj.rollnum)
##print(obj.fulldetail("GPAURAI"))

##class student:
##    def __init__(self):
##        self.name="Suraj"
##    def func(self):
##        return self.name
##obj=student()
##print(obj.func())


##class student:
##    def __init__(self):
##        self.name="Suraj"
##    def func(self,p):
##        self.other=p
##        return self.name+self.other
##obj=student()
##print(obj.func("Mishra"))




##class student:
##    def __init__(self):
##        self.name="Suraj"
##    def func(self):
##        self.other="Mishra"
##        return self.name+self.other
##obj=student()
##print(obj.func())



##class circle:
##    pi=3.14 #This is class variable access by class name
##    def __init__(self,radius):
##        self.radius=radius
##    def radius_calc(self):
##        return 2*circle.pi*self.radius #here we are access class variable throw class name
##obj=circle(2)
##print(obj.radius_calc())


#class method without argument

##class circle:
##    pi=3.14
##    
##    def __init__(self,radius):
##        self.radius=radius
##    def radius_calc(self):
##        return 2*circle.pi*self.radius
##    @classmethod
##    def class_func(cls):
##        return "This is class method",4*cls.pi
##obj=circle(2)
##print(obj.radius_calc())
##print(obj.class_func())
##print("Now calling with class name..........")
##print(circle.class_func())





#class method with argument

##class circle:
##    pi=3.14
##    
##    def __init__(self,radius):
##        self.radius=radius
##    def radius_calc(self):
##        return 2*circle.pi*self.radius
##    @classmethod
##    def class_func(cls,h):
##        cls.h=h       #This line is very important
##        return "This is class method",4*cls.pi*cls.h
##obj=circle(2)
##print(obj.radius_calc())
##print(obj.class_func(2))
##print("Now calling with class name..........")
##print(circle.class_func(3))


#static method

##class student:
##    def __init__(self,name):
##        self.name=name
##    @staticmethod
##    def func(a):
##        return f"and age is:{a}"
##obj=student("Mishra")
##print(obj.name)
##print(obj.func(20))

#with class variable

##class student:
##    age=12
##    def __init__(self,name):
##        self.name=name
##    @staticmethod
##    def func(a):
##        return f"Your name is:{a} and age is:{student.age}"
##obj=student("Mishra")
##print(obj.name)
##print(obj.func("Suraj"))








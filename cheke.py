import random
import pygame
i=0;
sum=0
print("THE CRICKET GAME")
a=random.randint(1,20)
print(f"Your target score is{a}")
print("your game is started")
while(i<6):
    b=int(input("enter any number beetween 1 to 6 enter:"))
    bat=random.randint(0,b)
    print(bat)
    sum=sum+bat
    d=a-sum
    if(sum==a):
        break
    else:
       print("hii")
    i+=1
    
    
print(f"Your first Over is Complete Your Score is{sum}; You Need {d} Runs for Win\n\n")
print("second over is started")

i=0;
sum=0
while(i<6):
    c=int(input("enter any number beetween 1 to 6 enter:"))
    bat=random.randint(0,b)
    print(bat)
    sum=sum+bat
    i+=1
print(f"Your second Over is Complete Your Score is{sum}; You Need {d-sum} Runs for Win")


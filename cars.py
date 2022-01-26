import pygame
import time
import random

def policecar(police_x,police_y,police): 	#define police function
    if police==0:		#at 0 stage
       police_come=pygame.image.load("car2.png")	#police car2 come
    if police==1:		#at 1 stage
       police_come=pygame.image.load("car3.png")	#police car3 come
    if police==2:
       police_come=pygame.image.load("car4.png")	#police car1 come
    gamewindow.blit(police_come,(police_x,police_y))
pygame.init()
screenheight=600
screenwidth=700
grey=(128,128,128)
red=(255,0,0)
car_width=23
gamewindow=pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("suraj mishra car racing")
carimg=pygame.image.load("car.png")
leftside=pygame.image.load("left.png")
rightside=pygame.image.load("right.png")
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])
    pygame.display.update()
    time.sleep(3)
    loop()
def background():
    gamewindow.blit(leftside,(0,0))
    gamewindow.blit(leftside,(600,0))
def car(x,y):
    gamewindow.blit(carimg,(x,y))
def loop():
    gameend=False
    x=400		
    y=540
    x_change=0
    y_change=0
    police_carspeed=9
    police_x=random.randrange(130,(600-car_width))
    police_y=-600
    police_width=23
    police_height=47
    police=0
    
    while not gameend:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                     x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
            if event.type==pygame.KEYUP:
                x_change=0 
	                
                    
        gamewindow.fill(grey)
        background()
        police_y-=police_carspeed/4
        policecar(police_x,police_y,police)
        police_y+=police_carspeed
        car(x,y)
        if x<130 or x>600-car_width:
            gameend=True
            text_screen("you crashed", red,270,250)
        if police_y>600:		
            police_y=0-police_height	
            police_x=random.randrange(130,(500))	 
            police=random.randrange(0,2)
        if y<police_y+police_height: 
            if x > police_x and x < police_x + police_width or x + car_width > police_x and x + car_width < police_x + police_width:
                text_screen("you crashed", red,270,250)
        x+=x_change    
        pygame.display.update()    
loop()                
pygame.quit()
quit()

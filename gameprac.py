import pygame
pygame.init()
import random

#GAME VARIABLE
screen_width=900
screen_height=600


#colors
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)

game_window=pygame.display.set_mode((screen_width,screen_height))
game_title=pygame.display.set_caption("SNAKE GAME")
pygame.display.update()

clock=pygame.time.Clock()

font=pygame.font.SysFont(None,50)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    game_window.blit(screen_text,[x,y])
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
def welcome():
    exit_game=False
    while not exit_game:
          game_window.fill(white)
          text_screen("welcome to snake",blue,250,270)
          text_screen("Press space bar for restart",blue,235,300)
          for event in pygame.event.get():
              if event.type==pygame.QUIT:
                 exit_game=True
              if event.type==pygame.KEYDOWN:
                  if event.key==pygame.K_SPACE:
                      game_loop()
          pygame.display.update()
          clock.tick(60)
    
        
 
#game loop
def game_loop():
   
    exit_game=False
    game_over=False
    snake_x=100
    snake_y=100
    x_velocity=5
    y_velocity=5
    snake_size=15
    fps=60
    score=0
    snk_list=[]
    snk_length=1 
    food_x=random.randint(0,screen_width/2)
    food_y=random.randint(0,screen_height/2)
            
    while not exit_game:
        if game_over:
            game_window.fill(white)
            text_screen("game over",red,screen_width/3,screen_height/3)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
            
        else:    
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        x_velocity=6
                        y_velocity=0
                        
                    if event.key==pygame.K_LEFT:
                        x_velocity=-6
                        y_velocity=0
                    if event.key==pygame.K_UP:
                        y_velocity=-6
                        x_velocity=0
                    if event.key==pygame.K_DOWN:
                        y_velocity=6
                        x_velocity=0
            snake_x=snake_x+x_velocity
            snake_y=snake_y+y_velocity
            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score+=1
                food_x=random.randint(0,screen_width/2)
                food_y=random.randint(0,screen_height/2)
                snk_length +=5
            game_window.fill(white)
            text_screen("score:"+str(score*10),red,5,5)
            pygame.draw.rect(game_window,red,[food_x,food_y,snake_size,snake_size])
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            if snake_x<0 or snake_x>screen_width and snake_y<0 or snake_y>screen_height:
                game_over=True
                print("game over")
            plot_snake(game_window, blue, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()

import pygame
import time
import random

#Setup
pygame.init()

textcolor=(0,0,0)
background_color=(200,200,225)
snake_color=(50,200,50)
food_color=(255,0,0)

width_of_screen=800
height_of_screen=600

snake_speed=30
block_size=10
clock=pygame.time.Clock()

font_style=pygame.font.SysFont("bahnschrift",25)

#Display settings
dis=pygame.display.set_mode([width_of_screen,height_of_screen])
pygame.display.set_caption("SNAKE")

def Score(score):
    message = font_style.render("Score: " + str(score),True,textcolor)
    dis.blit(message,[0,0])

def Snake(block_size,snake_list):
    for i in snake_list:
        pygame.draw.rect(dis,snake_color,[i[0],i[1],block_size,block_size])

def Game():
    starting_cordinates=[200,200]
    
    snake_list=[]
    Length_of_snake = 1
    score=Length_of_snake-1
    x1_change=0
    y1_change=0
    
    foodx=round(random.randrange(0,width_of_screen-block_size)/10)*10
    foody=round(random.randrange(0,height_of_screen-block_size)/10)*10
    
    game_over=False
    
    while not game_over:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    x1_change=0
                    y1_change=-block_size
                elif event.key==pygame.K_DOWN:
                    x1_change=0
                    y1_change=block_size
                elif event.key==pygame.K_RIGHT:
                    x1_change=block_size
                    y1_change=0
                elif event.key==pygame.K_LEFT:
                    x1_change=-block_size
                    y1_change=0
            
            if event.type == pygame.QUIT:
                game_over=True
        
        if starting_cordinates[0]<0 or starting_cordinates[0]>width_of_screen or starting_cordinates[1]<0 or starting_cordinates[1]>height_of_screen:
            game_over=True
        
        starting_cordinates[0]+=x1_change
        starting_cordinates[1]+=y1_change
        
        snake_Head=[]
        snake_Head.append(starting_cordinates[0])
        snake_Head.append(starting_cordinates[1])
        snake_list.append(snake_Head)
        if len(snake_list)>Length_of_snake:
            del snake_list[0]
        dis.fill(background_color)
        pygame.draw.rect(dis,food_color,[foodx,foody,block_size,block_size])
        
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_over=True
        
        Snake(block_size,snake_list)
        Score(score)
        pygame.display.update()
        if starting_cordinates[0]==foodx and starting_cordinates[1]==foody:
            foodx=round(random.randrange(0,width_of_screen-block_size)/10)*10
            foody=round(random.randrange(0,height_of_screen-block_size)/10)*10
            Length_of_snake+=1
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

Game()
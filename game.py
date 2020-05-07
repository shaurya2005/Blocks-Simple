

import pygame
import sys
import random

from pygame import mixer

pygame.init()

WIDTH = 1000
HEIGHT= 600

REDcolor=(250,0,0)
blue=(0,0,250)

player_pos=[300,500]

player_size=50

background_color=(0,0,0)
SPEED=10
enemy_size=50
enemy_ran=random.randint(0,WIDTH-enemy_size)
enemy_pos=[enemy_ran,0]

enemy_list=[enemy_pos]
score=0

myFont=pygame.font.SysFont("monospace",35)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
don=mixer.Sound("background.wav")

don.play(-1)

dash=mixer.music.load("gameover3.wav")
game_over=False
clock=pygame.time.Clock()

def level(score,SPEED):
    if score <10:
        SPEED=5
    elif  score<20:
        SPEED=8
    elif score<40:
        SPEED=11
    elif score<60:
        SPEED=14
    elif score<80:
        SPEED=16
    elif score<100:
        SPEED=18
    elif score<120:
        SPEED=20
    else :
        SPEED=24
    return SPEED


def drop_enemies(enemy_list):
    delay=random.random()
    if len(enemy_list)<11 and delay<0.1:

        x_pos=random.randint(0,WIDTH-enemy_size)
        y_pos=0
        enemy_list.append([x_pos,y_pos])
def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen,blue,(enemy_pos[0],enemy_pos[1],enemy_size,enemy_size))
def update_enemy_position(enemy_list,score):
    for idx, enemy_pos in enumerate(enemy_list):

        if enemy_pos[1] >=0 and enemy_pos[1]<HEIGHT:
            enemy_pos[1]+=SPEED
        else:
            enemy_list.pop(idx)
            score+=1
    return score
def collision_check(enemy_list,player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos,player_pos):
            return True
    return False


def detect_collision(player_pos,enemy_pos):
    p_x= player_pos[0]
    p_y=player_pos[1]

    e_x=enemy_pos[0]
    e_y=enemy_pos[1]
    if (e_x >= p_x and e_x < (p_x +player_size)) or (p_x >= e_x and p_x < (e_x+ enemy_size)):
        if (e_y >= p_y and e_y < (p_y+player_size)) or (p_y >=e_y and p_y < (e_y+enemy_size)):
            return True
    return False

while not game_over:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type ==pygame.KEYDOWN:

            x=player_pos[0]
            y=player_pos[1]

            if event.key == pygame.K_LEFT:

                x-=player_size


            elif event.key == pygame.K_RIGHT:
                x+=player_size
            player_pos=[x,y]
    screen.fill(background_color)
    #	if enemy_pos[1] >=0 and enemy_pos[1]<HEIGHT:
    #		enemy_pos[1]+=SPEED
    #	else:
    #		enemy_pos[0]=random.randint(0,WIDTH-enemy_size)
    #		enemy_pos[1]=0
    #
    if detect_collision(player_pos,enemy_pos):

        mixer.music.load("gameover3.wav")
        mixer.music.play(-1)
        game_over=False



    drop_enemies(enemy_list)
    score=update_enemy_position(enemy_list,score)
    SPEED=level(score,SPEED)
    text="Score:"+str(score)
    label=myFont.render(text,1,(255,255,0))
    screen.blit(label,(WIDTH-200,HEIGHT-40))



    if collision_check(enemy_list,player_pos):
        das=mixer.Sound("gameover3.wav")
        das.play(-1)

        game_over=True
    draw_enemies(enemy_list)


    pygame.draw.rect(screen,REDcolor,(player_pos[0],player_pos[1],player_size,player_size))
    clock.tick(30)
    pygame.display.update()


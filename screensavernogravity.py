import pygame as pg #kolja
import time
import random
running=True
pg.key.get_pressed
WIDTH=1366
HEIGHT=768
background=(0,0,0)
vbirdx=1
vbird=1
counterstike="lol"
t=0.01
birdw=99.86
birdy=100
birdx=600

ballr=0
ballcx=600
ballcy=100
ballv=1
ballvx=1

pg.display.set_caption("screensaver")
screen=pg.display.set_mode((WIDTH,HEIGHT))
satic=pg.time.Clock()

screen.fill(background)

while running:
    boja=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False

    if birdy+birdw>=HEIGHT:
        vbird*=-1
    if birdx<=0:
        vbirdx*=-1
    if birdx+birdw>=WIDTH:
        vbirdx*=-1
    if birdy<=0:
        vbird=vbird*(-1)
    birdy+=vbird
    birdx+=vbirdx
    vbird+=0.001
    pg.draw.rect(screen,(boja),(birdx,birdy,birdw,birdw))
    pg.display.update()
pg.quit
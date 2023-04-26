import pygame
from pygame.draw import *

def draw_body(surface,x,y,width,height,color):
    ellipse(surface,color,(x-width//2,y-height//2,width,height))
    

def draw_head(surface,x,y,width,height,color):
    circle(surface,color,(x,y),height//2)
    

def draw_ear(surface,x,y,width,height,color):
    ellipse(surface,color,(x-width//2,y-height//2,width,height))
    

def draw_leg(surface,x,y,width,height,color):
    ellipse(surface, color, (x-width//2,y-height//2,width,height))
    


def draw_hare(surface,x,y,width,height,color):
    draw_body(surface,x,y + height//4,width//2,height//2,color)
    draw_head(surface,x,y-height//8,height//4,color)
    for ear_x in (x-height//16,x+height//16):
        draw_ear(surface,ear_x,y-height//2 + height//8,width//8,height//3,color)
    for leg_x in (x-width//4,x+width//2):
        draw_leg(surface,leg_x,y+height//2 - leg_height//2,width//4,leg_height,color)
    

def draw_rabbit(surfece,x,y,width,height,color):
    draw_body(surfece,x,y,width//4,height//4,(155,155,100))
    draw_head(surfece,x,0.8*y,width//8,height//8,(155,155,100))
    draw_ear(surfece,1.1*x,0.7*y,width//10,height//16,(255,255,0))
    draw_ear(surfece,0.9*x,0.7*y,width//10,height//16,(255,255,0))
    draw_leg(surfece,0.9*x,1.3*y,width//8,height//6,color)
    draw_leg(surfece,1.1*x,1.3*y,width//8,height//6,color)


pygame.init()

FPS = 60
screen = pygame.display.set_mode((400,400))

draw_rabbit(screen,200,200,200,400,(200,200,200))

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished =  True
pygame.quit()

import pygame
from pygame.locals import *
import math
import random

RED=(255,0,128)
BLUE=(53,226,242)
YELLOW=(246,223,14)
PURPLE=(140,19,251)

#color1=RED
N=(0,0,0)
w=400
h=600



arc_surface=list
#FAIRE UNE LISTE D'OBSTACLE A LA FIN !!

    
    
def balle():
    balle_surface=pygame.Surface((20,20))
    balle_surface.fill(N)
    balle_surface.set_colorkey(N)#transparence du surface
    return balle_surface

def draw_balle(balle_surface,color):
    pygame.draw.circle(balle_surface,color,(10,10),10)

def balle_rect():
    balle_surface=balle()
    balle_rect=balle_surface.get_rect()
    balle_rect.center=(w/2,500)
    return balle_rect

def obst_cercle_surf():
    arc_surface=pygame.Surface((150,150))
    arc_surface.fill((N))
    arc_surface.set_colorkey((N))
    
    return arc_surface

def draw_obst_cercle(arc_surface,i):
    col=math.radians(270)
    k=math.radians(360)
    x_P=math.radians(0)
    y_P=math.radians(90)
    x_R=math.radians(90)
    y_R=math.radians(180)
    x_Y=math.radians(180)
    y_Y=math.radians(270)
    x_B=math.radians(270)
    y_B=math.radians(360)

    x_P+=i
    y_P+=i
     
    x_R+=i
    y_R+=i
    
    
    x_Y+=i    
    y_Y+=i
    
    
    x_B+=i
    y_B+=i
    


    pygame.draw.arc(arc_surface,(RED),[0,0,150,150],x_R,y_R,10)
    pygame.draw.arc(arc_surface,(PURPLE),[0,0,150,150],x_P,y_P,10)
    pygame.draw.arc(arc_surface,(BLUE),[0,0,150,150],x_B,y_B,10)
    pygame.draw.arc(arc_surface,(YELLOW),[0,0,150,150],x_Y,y_Y,10)

    

    
def cercle_change_color():
    pie=pygame.image.load("pie_circle.png")
    pie=pie.convert_alpha()
    return pie


def obst_carre():

    carre_surf=pygame.Surface((125,125))
    carre_surf.fill((N))
    carre_surf.set_colorkey((N))
    pygame.draw.line(carre_surf,RED,(0,0),(125,0),20)
    pygame.draw.line(carre_surf,PURPLE,(0,0),(0,125),20)
    pygame.draw.line(carre_surf,BLUE,(0,125),(125,125),20)
    pygame.draw.line(carre_surf,YELLOW,(125,0),(125,125),20)
    return carre_surf
    

def obst_ligne(dec):
    colorBarre=[RED,RED,RED,BLUE,BLUE,BLUE,YELLOW,YELLOW,YELLOW,PURPLE,PURPLE,PURPLE]
    
    ligne_surf=pygame.Surface((400,30))
    #ligne_surf.fill((N))
    #ligne_surf.set_colorkey((N))
    
    pygame.draw.line(ligne_surf, colorBarre[(0+dec)%12],(0,0),(33,0),20)
    pygame.draw.line(ligne_surf, colorBarre[(1+dec)%12], (34,0),(66,0),20)
    pygame.draw.line(ligne_surf, colorBarre[(2+dec)%12], (67,0),(100,0),20)
    pygame.draw.line(ligne_surf, colorBarre[(3+dec)%12], (101,0),(133,0),20)
    pygame.draw.line(ligne_surf, colorBarre[(4+dec)%12],(134,0),(166,0),20)## collision
    pygame.draw.line(ligne_surf, colorBarre[(5+dec)%12], (167,0),(200,0),20)##collision
    pygame.draw.line(ligne_surf, colorBarre[(6+dec)%12], (201,0),(233,0),20)
    pygame.draw.line(ligne_surf, colorBarre[(7+dec)%12], (234,0),(266,0),20)
    pygame.draw.line(ligne_surf, colorBarre[(8+dec)%12],(267,0),(300,0),20)
    pygame.draw.line(ligne_surf, colorBarre[(9+dec)%12], (301,0),(333,0),20)
    pygame.draw.line(ligne_surf, colorBarre[(10+dec)%12], (334,0),(366,0),20)
    pygame.draw.line(ligne_surf, colorBarre[(11+dec)%12], (367,0),(400,0),20)
    return ligne_surf


def play():
    play=pygame.image.load("play.png")
    play=play.convert_alpha()
    return play

def retry():
    retry=pygame.image.load("retry.png")
    retry=retry.convert_alpha()
    return retry

    



	


 

import pygame
from pygame.locals import *
import math
import random

RED=(255,0,128)
BLUE=(53,226,242)
YELLOW=(246,223,14)
PURPLE=(140,19,251)
colors=[RED,BLUE,YELLOW,PURPLE]
color1=RED
N=(0,0,0)
w=800
h=600
PI=math.pi
x1=float(PI/2)
y1=float(PI)
x2=0.0
x3=float(3*PI/2)
y3=float(2*PI)
<<<<<<< HEAD
arc_surface=list
#FAIRE UNE LISTE D'OBSTACLE A LA FIN !!
=======


def newColor(): #DOES NOT WORK 
	rd=random.randrange(0,4,1)
	color1=colors[rd]
	balle()		
>>>>>>> 15b52778180d41cecd303e329e0dfd79adaa07f6
    
def balle():
    balle_surface=pygame.Surface((20,20))
    balle_surface.fill(BLUE)
    balle_surface.set_colorkey(BLUE)#transparence du surface
    pygame.draw.circle(balle_surface,color1,(10,10),10)
    return balle_surface

def balle_rect():
    balle_surface=balle()
    balle_rect=balle_surface.get_rect()
    balle_rect.center=(w/2,500)
    return balle_rect

def obst_cercle_surf():
    arc_surface=pygame.Surface((250,250))
    arc_surface.fill((N))
    arc_surface.set_colorkey((N))
    
    return arc_surface

def draw_obst_cercle(arc_surface,i):
    
    pygame.draw.arc(arc_surface,(RED),[0,0,250,250],x1+i,y1+i,10)
    pygame.draw.arc(arc_surface,(PURPLE),[0,0,250,250],x2+i,x1+i,10)
    pygame.draw.arc(arc_surface,(BLUE),[0,0,250,250],x3+i,y3+i,10)
    pygame.draw.arc(arc_surface,(YELLOW),[0,0,250,250],y1+i,x3+i,10)
    

<<<<<<< HEAD

def obst_carre_surf():
    carre_surf=pygame.Surface((250,250))
    carre_surf.fill((N))
    arc_surface.set_colorkey((N))
    return carre_surf

#def draw_obst_carre(carre_surf):
 #   pygame.draw.line(carre_surf,(RED),)









=======
    return arc_surface
    
def obst_carre():
	w=400
	h=300
	x=20
	carre_surface=pygame.Surface((250,250))
	carre_surface.fill((N))
	carre_surface.set_colorkey((N))
	pygame.draw.line(carre_surface,RED,(w-x,h+x),(w+x,h+x),1)
	pygame.draw.line(carre_surface,BLUE,(w-x,h+x),(w-x,h-x),1)
	pygame.draw.line(carre_surface,YELLOW,(w-x,h-x),(w+x,h-x),1)
	pygame.draw.line(carre_surface,PURPLE,(w+x,h+x),(w+x,h-x),1)
	
	return carre_surface
>>>>>>> 15b52778180d41cecd303e329e0dfd79adaa07f6

	


 

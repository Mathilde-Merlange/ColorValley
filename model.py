import view
import math
import random
import pygame
from pygame.locals import *

RED=(255,0,128)
BLUE=(53,226,242)
YELLOW=(246,223,14)
PURPLE=(140,19,251)
BLACK=(0,0,0)



def ball_gravity(y,y_init):
    if(y<=y_init):
            y+=2
    return y


def update_ball(surface):
    color=newColor()
    view.draw_balle(surface,color)

def couleur_arc_bas(i):

    col_bas=math.radians(270)
    #col_haut=math.radians(90)
    
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
    if (y_P>col_bas) and (x_P <col_bas):
       # print ("PURPLE")
        return PURPLE 
    x_R+=i
    y_R+=i
    
    if (y_R>col_bas) and (x_R <col_bas):
        #print("RED")
        return RED 

    x_Y+=i    
    y_Y+=i
    
    if (y_Y>col_bas) and (x_Y <col_bas):
        #print("YELLOW")
        return YELLOW

    x_B+=i
    y_B+=i
    if (y_B>col_bas) and (x_B <col_bas):
       # print("BLUE")
        return BLUE

def couleur_arc_haut(i):
    
    col_haut=math.radians(450)
    
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
    if (y_P>math.radians(90)) and (x_P <math.radians(90)):
        return PURPLE 



    x_R+=i
    y_R+=i
    
    if (y_R>col_haut) and (x_R <col_haut):
        return RED 


    x_Y+=i    
    y_Y+=i
    
    if (y_Y>col_haut) and (x_Y <col_haut):
        return YELLOW

    x_B+=i
    y_B+=i
    if (y_B>col_haut) and (x_B <col_haut):
        return BLUE



def collision(rectA, rectB):
    if rectB.right < rectA.left:
        # rectB est à gauche
        return False
    if rectB.bottom < rectA.top:
        # rectB est au-dessus
        return False
    if rectB.left > rectA.right:
        # rectB est à droite
        return False
    if rectB.top > rectA.bottom:
        # rectB est en-dessous
        return False
    # Dans tous les autres cas il y a collision
    return True
	

#def coll_color(balle,chg_color):
	#if (collision(balle,chg_color)):
		#view.newColor()
		
def coll_cercle(balle,cercle,couleur_arc,colorBall):
    if (collision(balle,cercle) and (colorBall==couleur_arc)):
        #print("collision cercle")
        return True
    else :
        return False
		
def score_add(score):
    score+=1
    	

def newColor():
    colors=[RED,BLUE,YELLOW,PURPLE]
    color1=random.choice(colors)
    return color1	


def rotate_cercle(i,obst_cercle_surf):
    if(i>math.radians(360)):
            i=0.0
    else:
            i+=math.radians(2)
        
    view.draw_obst_cercle(obst_cercle_surf,i)
    return i

def rotate_carre(i):
    if (i>360):
        i=0
    else:
          i+=2
    return i

def coll_pie(balle_surf,balle,pie,score):
   if (collision(balle,pie)):
    pie.y=-150
    update_ball(balle_surf)
    score_add(score)
    
   return pie.y


def couleur_carre(i):
    col_bas=135
    x_P=0
    y_P=90
    x_B=90
    y_B=180
    x_Y=180
    y_Y=270
    x_R=270
    y_R=360

    



    if(x_P>=360):
        x_P=0

    if(y_P>=360):
        y_P=0

    x_P+=i
    y_P+=i
    if (y_P>col_bas) and (x_P <col_bas):
        
        print ("PURPLE")

    if(x_B>=360):
        x_B=0

    if(y_B>=360):
        y_B=0


    x_B+=i
    y_B+=i
    if (y_B>col_bas) and (x_B <col_bas):
        print("BLUE")


    if(x_Y>360):
        x_Y=0

    if(y_Y>360):
        y_Y=0

    x_Y+=i    
    y_Y+=i
    
    if (y_Y>col_bas) and (x_Y <col_bas):
        print("YELLOW")


    if(x_R>360):
        x_R=0

    if(y_R>360):
        y_R=0

    x_R+=i
    y_R+=i
    
    if (y_R>col_bas) and (x_R <col_bas):
        print("RED")

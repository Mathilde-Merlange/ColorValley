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
            y+=5
    return y


def update_ball(surface):
    color=newColor()
    view.draw_balle(surface,color)
    return color


def newColor():
    colors=[BLUE,RED,YELLOW,PURPLE]
    c1=random.choice(colors)
    #print ("couleur balle = ",c1)
    return c1

def couleur_arc_bas(i):

    col_bas=math.radians(270)
    
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

    

    if (y_P>col_bas) and (x_P <col_bas):
        #print ("PURPLE	   b")
        return PURPLE 
    
    
    if (y_R>col_bas) and (x_R <col_bas):
        #print("RED	   b")
        return RED 

    
    
    if (y_Y>col_bas) and (x_Y <col_bas):
        #print("YELLOW	   b")
        return YELLOW

    
    
    if (y_B>math.radians(630)) and (x_B <math.radians(630)):
        #print("BLUE	   b")
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
        #print("PURPLE	h")
        return PURPLE 



    x_R+=i
    y_R+=i
    
    if (y_R>col_haut) and (x_R <col_haut):
        #print("RED	h")
        return RED 


    x_Y+=i    
    y_Y+=i
    
    if (y_Y>col_haut) and (x_Y <col_haut):
        #print("YELLOW	h")
        return YELLOW

    x_B+=i
    y_B+=i

    if (y_B>col_haut) and (x_B <col_haut):
        #print("BLUE	h")

        return BLUE
    


def collision_bas(rectA, rectB):
       ###and (rectA.top > (rectB.top+10))
    if(rectB.bottom < rectA.top):
        return False
    if((rectA.bottom < (rectB.bottom-10)) ):
        return False
    return True
    

def collision_haut(rectA,rectB):
    if(rectA.bottom<rectB.top):
        return False
    if(rectA.top>(rectB.top+10)):
        return False
    return True

def collision(rectA,rectB):
    if rectB.right < rectA.left:
        #rectB est à gauche
        return False
    if rectB.bottom < rectA.top:
        #rectB est au-dessus
        return False
    if rectB.left > rectA.right:
        #rectB est à droite
        return False
    if rectB.top > rectA.bottom:
        #rectB est en-dessous
        return False
    # Dans tous les autres cas il y a collision
    return True

        
def coll_balle_obs_bas(balle,rect_obst,couleur_obst,colorBall):
    if (collision_bas(balle,rect_obst) and (colorBall==couleur_obst)):
        #print("collision")
        return True
    else :
        if(collision_bas(balle,rect_obst) and (colorBall!=couleur_obst)):
            #print ("perdu")
    
            return False
    return True

def coll_balle_obs_haut(balle,rect_obst,couleur_obst,colorBall):
    if (collision_haut(balle,rect_obst) and (colorBall==couleur_obst)):
        #print("collision")
        return True
    else :
        if(collision_haut(balle,rect_obst) and (colorBall!=couleur_obst)):
            #print ("perdu")
            return False            
    return True
def score_add(score):
    score+=1
    return score
        
def coll_ligne(balle,ligne,c5,c6,colorBalle):
	if (c5!=c6) and collision(balle,ligne):
		return True
	else:
		if (c5!=colorBalle) and collision(balle,ligne):
			return True
		if (c5==colorBalle) and collision(balle,ligne):
			return False



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



def couleur_carre_bas(i):
    col_bas=135
    x_P=0
    y_P=90
    x_B=90
    y_B=180
    x_Y=180
    y_Y=270
    x_R=270
    y_R=360

    
    
    x_P+=i
    y_P+=i
    x_B+=i
    y_B+=i  
    x_Y+=i
    y_Y+=i
    x_R+=i
    y_R+=i

    if(x_P>360):
        x_P=0
        x_P+=i

    if(y_P>360):
        y_P=0
        y_P+=i-270

    if(x_B>360):
        x_B=0
        x_B+=i-270

    if(y_B>360):
        y_B=0
        y_B+=i-180

    if(x_Y>360):
        x_Y=0
        x_Y+=i-180

    if(y_Y>360):
        y_Y=0
        y_Y+=i-90

    if(x_R>360):
        x_R=0
        x_R+=i-90

    if(y_R>360):
        y_R=0
        y_R+=i
      


    if (y_P>col_bas) and (x_P <col_bas):
        #print("PURPLE")
        return PURPLE 
    
    
    if (y_R>col_bas) and (x_R <col_bas):
        #print("RED")
        return RED 

   
    
    if (y_Y>col_bas) and (x_Y <col_bas):
        #print("YELLOW")
        return YELLOW

    
    if (y_B>col_bas) and (x_B <col_bas):
        #print("BLUE")
        return BLUE


def couleur_carre_haut(i):
    col_haut=315
    x_P=0
    y_P=90
    x_B=90
    y_B=180
    x_Y=180
    y_Y=270
    x_R=270
    y_R=360

    
    
    x_P+=i
    y_P+=i
    x_B+=i
    y_B+=i  
    x_Y+=i
    y_Y+=i
    x_R+=i
    y_R+=i

    if(x_P>360):
        x_P=0
        x_P+=i

    if(y_P>360):
        y_P=0
        y_P+=i-270

    if(x_B>360):
        x_B=0
        x_B+=i-270

    if(y_B>360):
        y_B=0
        y_B+=i-180

    if(x_Y>360):
        x_Y=0
        x_Y+=i-180

    if(y_Y>360):
        y_Y=0
        y_Y+=i-90

    if(x_R>360):
        x_R=0
        x_R+=i-90

    if(y_R>360):
        y_R=0
        y_R+=i
      


    if (y_P>col_haut) and (x_P <col_haut):
        
        return PURPLE 
    
    
    if (y_R>col_haut) and (x_R <col_haut):
        
        return RED 

   
    
    if (y_Y>col_haut) and (x_Y <col_haut):
        
        return YELLOW

    
    if (y_B>col_haut) and (x_B <col_haut):
        
        return BLUE   

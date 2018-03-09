import view


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
	
def coll_score(balle,barre_score):
	if (collision(balle,barre_score)):
		score=score_add()
		
def coll_color(balle,chg_color):
	if (collision(balle,chg_color)):
		view.newColor()
		
	
		
def score_add():
	score+=1		

from graphics import *
from classes import *
import time

x = 1200
y = 600
raio = 15
gameFPS = 30
framePeriod = 1.0/gameFPS
charVel = 10
ground = 545


# Main Window
win = GraphWin('Head Soccer', x, y, False)

# Instance background but don't draw
background = Image(Point(x/2, y/2), 'Imagens/bg.gif')

# Init Key Buffer
win.ligar_Buffer()

# Instance Player and draw collisions ## Collisions must be drawed before background
leftPlayer = Player(win, 300, 485)
leftPlayer.drawCollisions(300, 485)

# Instance Ball and collisions
ball = Ball(win, x/2, ground - ballRadius)
ball.drawCollisions(x/2, ground - ballRadius)

# Draw background
background.draw(win)

# Draw Player Mechs
leftPlayer.drawMech(300, 503, "Imagens/LeftChar.gif")

# Draw Ball Mechs
ball.drawMech(x/2, ground - ballRadius, "Imagens/Ball.gif")



# Main loop
while True:

    # Get all Pressed Keys
    lista = win.checkKey_Buffer()
    update()


    # Keyboard Verification
    if len(lista) > 0:

        if ("Left" in lista) and (leftPlayer.getPos()[0] - headRadius > 0):
            leftPlayer.move(-charVel, 0)

        if("Right" in lista) and (leftPlayer.getPos()[0] + headRadius < x):	
            leftPlayer.move(charVel, 0)
            
        if("Up" in lista):	
            if not(leftPlayer.isJumping):
                leftPlayer.isJumping = True

        if("quoteright" in lista):	
            leftPlayer.restartPos()
    
    if ( checkCollisions(leftPlayer, ball) ):
        
        # if True: Char is left from ball
        if ( leftPlayer.getFootPos()[0] < ball.getPos()[0] ):
            ball.move(50, 0)

    # leftPlayer Jump Verification
    if (leftPlayer.isJumping):

        if leftPlayer.contJump <= 24:

            if leftPlayer.contJump//12 == 0:
                leftPlayer.jump(-leftPlayer.jumpDy)
                leftPlayer.jumpDy += 1.5

            if leftPlayer.contJump//12 == 1:
                leftPlayer.jumpDy -= 1.5
                leftPlayer.jump(leftPlayer.jumpDy)

            leftPlayer.contJump += 1 		
        else:
            leftPlayer.isJumping = False
            leftPlayer.contJump = 0
	

    time.sleep(framePeriod)

win.close()
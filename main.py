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
friction = 1


# Main Window
win = GraphWin('Head Soccer', x, y, False)

# Instance background but don't draw
background = Image(Point(x/2, y/2), 'Images/bg.gif')

# Init Key Buffer
win.ligar_Buffer()


##### INSTANCE AND DRAW COLLISIONS ######

# Instance Player and draw collisions ## Collisions must be drawed before background
leftPlayer = Player(win, 300, 485)
leftPlayer.drawCollisions(900, 485)

# Instance Ball and collisions
ball = Ball(win, x/2, ground - ballRadius)
ball.drawCollisions(x/2, ground - ballRadius - 500)


##### DRAW BACKGROUND #####
 
background.draw(win)


##### DRAW MECHS #####

# Draw Player Mechs
leftPlayer.drawMech(300, 503, "Images/LeftChar.gif")

# Draw Ball Mechs
ball.drawMech(x/2, ground - ballRadius - 500, "Images/Ball.gif")



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
            ball.restartPos()
    

    # Foot and Ball collisions
    if ( checkCollisions(leftPlayer, ball) ):
        
        # if True: Char is left from ball
        if ( leftPlayer.getFootPos()[0] < ball.getPos()[0] ):
            ball.ballVelocityX = 20

        # if True: Char is right from ball
        if ( leftPlayer.getFootPos()[0] > ball.getPos()[0] ):
            ball.ballVelocityX = -20


    # leftPlayer Jump Verification
    if (leftPlayer.isJumping):

        if leftPlayer.contJump <= 24:

            # Up
            if leftPlayer.contJump//12 == 0:
                leftPlayer.jump(-leftPlayer.jumpDy)
                leftPlayer.jumpDy += 1.5

            # Down
            if leftPlayer.contJump//12 == 1:
                leftPlayer.jumpDy -= 1.5
                leftPlayer.jump(leftPlayer.jumpDy)

            leftPlayer.contJump += 1 

        # Jump ends		
        else:
            leftPlayer.isJumping = False
            leftPlayer.contJump = 0


    print( getAngle(leftPlayer, ball) )

    # Checks for vel and move
    if (ball.ballVelocityX != 0 or ball.ballVelocityY != 0):

        ball.move(ball.ballVelocityX, ball.ballVelocityY)

        # Verify if ball is on the ground and apply friction
        if ( ball.getPos()[1] + ballRadius == ground ):

            # Verify if ball is moving to right
            if ball.ballVelocityX > 0:
            
                if (ball.ballVelocityX - friction < 0):
                    ball.ballVelocityX = 0
                else:
                    ball.ballVelocityX -= friction
            
            # Or moving to left
            else:

                if (ball.ballVelocityX + friction > 0):
                    ball.ballVelocityX = 0
                else:
                    ball.ballVelocityX += friction


	

    time.sleep(framePeriod)

win.close()
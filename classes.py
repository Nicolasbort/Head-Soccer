
from graphics import *
import math


global footRadius
global headRadius
global heightJump
global ballRadius

footRadius = 15
headRadius = 28
heightJump = 24
ballRadius = 15


# Verify foot and ball collisions
def checkCollisions(objFoot, ballObj):

    distance = math.hypot( ballObj.getPos()[0] - objFoot.getFootPos()[0] , ballObj.getPos()[1] - objFoot.getFootPos()[1])

    if (distance <= footRadius + ballRadius):
        return True




class Ball():
    def __init__(self, frame, initX, initY):

        #Ball Frame
        self.frame = frame
        
        # Ball Velocity
        self.ballVelocityX = 0
        self.ballVelocityY = 0

        # Initial parameters
        self.initX = initX
        self.initY = initY

    
    def move(self, dx, dy):
        self.circleBall.move(dx, dy)
        self.mech.move(dx, dy)


    def getPos(self):
        return self.circleBall.getCenter().getX(), self.circleBall.getCenter().getY() 
        
    
    def drawCollisions(self, px, py):
        self.circleBall = Circle(Point(px, py), ballRadius)
        self.circleBall.draw(self.frame)

    
    def drawMech(self, px, py, path):
        self.mech = Image(Point(px, py), path)
        self.mech.draw(self.frame)

    
    def restartPos(self):
        # Restart init values
        self.ballVelocityX = 0
        self.ballVelocityY = 0

        # Restart Ball Position
        self.move( self.initX - self.getPos()[0], self.initY - self.getPos()[1] )


class Player():
    def __init__(self, frame, initX, initY, charVel = 10):

        # Player Frame
        self.frame = frame

        # Bool Values
        self.isJumping = False
        self.isKicking = False

        # Init Parameters
        self.initX = initX
        self.initY = initY
        self.jumpDy = 1
        self.contJump = 0


    # Draw Char collisions
    def drawCollisions(self, px, py):
        self.head = Circle(Point(px, py), headRadius)
        self.head.draw(self.frame)
        self.foot = Circle(Point(px, py + 45), footRadius)
        self.foot.draw(self.frame)


    # Draw Char image (.gif)
    def drawMech(self, px, py, path):
        self.mech = Image(Point(px, py), path)
        self.mech.draw(self.frame)


    # Move Char
    def move(self, dx, dy):
        self.head.move(dx, dy)
        self.foot.move(dx, dy)
        self.mech.move(dx, dy)


    # Jump Char
    def jump(self, dy):
        self.move(0, dy)


    # Get X and Y Player Position ([X, Y])
    def getPos(self):
        return self.head.getCenter().getX(), self.head.getCenter().getY()


    def restartPos(self):
        # Restart init Parameters
        self.isJumping = False
        self.isKicking = False
        self.jumpDy = 1
        self.contJump = 0

        # Restart Player init Position
        self.move(self.initX - self.getPos()[0], self.initY - self.getPos()[1])


    def getFootPos(self):
        return self.foot.getCenter().getX(), self.foot.getCenter().getY() 

#class Goalpost():

#class Scoreboard():


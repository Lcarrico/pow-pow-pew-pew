from pygame import Surface
import pygame
from gun import gun
import math
from shapely.geometry import Polygon
import utils
from time import time

X = 0
Y = 1
radTwoOverTwo = (2**(1/2))/2

class player():
    def __init__(self, x:int, y:int, radius:float, color:list, direction:float, speed:float, screen:Surface, lives:float = 3):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.speed = speed
        self.screen = screen
        self.lives = lives
        self.movingLeft = False
        self.movingRight = False
        self.movingUp = False
        self.movingDown = False
        self.image = pygame.image.load('player-handgun-extraspace-antialias.png')
        self.image = pygame.transform.smoothscale(self.image, [self.radius*10, self.radius*10])
        self.canShoot = True
        self.lastShotTime = -1
        self.shooting = False
        self.kills = 0
        # self.image = pygame.transform.rotate(self.image, math.degrees(-math.pi/2))



        gunWidth = 33
        gunHeight = 8
        anchor = [x, y]
        p1 = [x, y+radius]
        p2 = [x+gunWidth, y+radius]
        p3 = [x+gunWidth, y+radius+gunHeight]
        p4 = [x, y+radius+gunHeight]
        muzzle = [x+gunWidth, y+radius+(gunHeight/2)]
        gunColor = [47, 237, 92]
        gunDirection = 0
        self.gun1 = gun(anchor, [p1,p2,p3,p4], gunWidth, gunHeight, gunDirection, gunColor, muzzle, screen)

        # gunWidth = 20
        # gunHeight = 10
        # anchor = [x, y]
        # p1 = [x, y-radius]
        # p2 = [x+gunWidth, y-radius]
        # p3 = [x+gunWidth, y-radius-gunHeight]
        # p4 = [x, y-radius-gunHeight]
        # muzzle = [x+gunWidth, y-radius-(gunHeight/2)]
        # gunColor = [47, 237, 92]
        # gunDirection = 0
        # self.gun2 = gun(anchor, [p1,p2,p3,p4], gunWidth, gunHeight, gunDirection, gunColor, muzzle, screen)
    
    def canMove(self, game, xDis, yDis):
        tmpCircle = {'x':game.width/2 , 'y':game.height/2 , 'radius':self.radius}
        insets = game.cameraHandler.getInsets()

        collisionGroups = game.worldHandler.collisionGroups
        for collisionGroup in collisionGroups:
            for collision in collisionGroup:

                tmpRect = {'x':collision['x'] + collision['width']/2 + insets[X] - xDis * self.speed, 'y':collision['y'] + collision['height']/2 + insets[Y] - yDis * self.speed, 
                            'width':collision['width'], 'height':collision['height']}
                if utils.circleIntersectsRectangle(tmpCircle, tmpRect):
                    return False
        return True

    def move(self, game, xDis:int=1, yDis:int=1):

        if self.canMove(game, xDis, yDis):
            self.x += xDis * self.speed
            self.y += yDis * self.speed

            gunXDis = xDis * self.speed
            gunYDis = yDis * self.speed

            self.gun1.move(gunXDis, gunYDis)
            # self.gun2.move(gunXDis, gunYDis)

    def loseLife(self, lives):
        self.lives -= lives
    
    def update(self, game):
        if self.movingLeft and self.movingUp:
            self.move(game, -radTwoOverTwo, 0)
            self.move(game, 0, -radTwoOverTwo)
        elif self.movingUp and self.movingRight:
            self.move(game, 0, -radTwoOverTwo)
            self.move(game, radTwoOverTwo, 0)
        elif self.movingRight and self.movingDown:
            self.move(game, radTwoOverTwo, 0)
            self.move(game, 0, radTwoOverTwo)
        elif self.movingDown and self.movingLeft:
            self.move(game, 0, radTwoOverTwo)
            self.move(game, -radTwoOverTwo, 0)
        elif self.movingLeft:
            self.move(game, -1, 0)
        elif self.movingRight:
            self.move(game, 1, 0)
        elif self.movingUp:
            self.move(game, 0, -1)
        elif self.movingDown:
            self.move(game, 0, 1)

        worldWidth = game.worldHandler.width
        worldHeight = game.worldHandler.height

        if self.x - self.radius < 0:
            self.setX(self.radius)
        
        if self.y - self.radius < 0:
            self.setY(self.radius)

        if self.y + self.radius > worldHeight:
            self.setY(worldHeight - self.radius)
        
        if self.x + self.radius > worldWidth:
            self.setX(worldWidth - self.radius)

        insets = game.cameraHandler.getInsets()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.turnTo(mouse_x - insets[X], mouse_y - insets[Y])

        if time() - self.lastShotTime > 0.25:
            self.canShoot = True
        
        if self.canShoot and self.shooting:
            self.shoot(game)

        self.gun1.update(game)
        # self.gun2.update(game)

    def draw(self, game):
        insets = game.cameraHandler.getInsets()
        

        tmpImage = pygame.transform.rotate(self.image, math.degrees(-self.direction))
        new_rect = tmpImage.get_rect(center = self.image.get_rect(center = (300, 300)).center)
        new_rect.update(round(new_rect.left + self.x + insets[X] - 300), round(new_rect.top + self.y + insets[Y] - 300), new_rect.width, new_rect.height)

        game.screen.blit(tmpImage, new_rect)
        # pygame.draw.circle(self.screen, 'blue', [self.x+insets[X], self.y+insets[Y]], self.radius, 2)

        self.gun1.draw(game)
        # self.gun2.draw(game)


    def setX(self, x):
        self.x = x
        self.gun1.setAnchor([self.x, self.y])
        # self.gun2.setAnchor([self.x, self.y])
    
    def setY(self, y):
        self.y = y
        # self.gun1.setAnchor([self.x, self.y])
        self.gun2.setAnchor([self.x, self.y])

    def turnTo(self, turnX, turnY):
        newDir = math.atan2(turnY-self.y, turnX-self.x)
        self.direction = newDir

        self.gun1.setDirection(newDir)
        # self.gun2.setDirection(newDir)

    def shoot(self, game):
        if self.canShoot:
            game.soundHandler.playSound('gunshot2.wav')
            self.gun1.shoot()
            self.lastShotTime = time()
            self.canShoot = False
            # self.gun2.shoot()

    def getBullets(self):
        return self.gun1.bullets # + self.gun2.bullets

    def startMovingLeft(self):
        self.movingLeft = True
    
    def stopMovingLeft(self):
        self.movingLeft = False

    
    def startMovingUp(self):
        self.movingUp = True
    
    def stopMovingUp(self):
        self.movingUp = False


    def startMovingDown(self):
        self.movingDown = True
    
    def stopMovingDown(self):
        self.movingDown = False


    def startMovingRight(self):
        self.movingRight = True
    
    def stopMovingRight(self):
        self.movingRight = False
    
    def startSprinting(self):
        self.speed *= 1.5
    
    def stopSprinting(self):
        self.speed /= 1.5

    def startShooting(self, game):
        self.shooting = True

    def stopShooting(self, game):
        self.shooting = False
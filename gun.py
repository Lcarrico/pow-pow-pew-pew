from pygame import Surface
import pygame
from math import dist, sin, cos
from bullet import bullet
from copy import deepcopy
X = 0
Y = 1

class gun():
    def __init__(self, anchor:list, points:list, width:int, height:int, direction:float, color:list, muzzle:list, screen:Surface):
        self.anchor = anchor
        self.points = points
        self.width = width
        self.height = height
        self.direction = direction
        self.color = color
        self.screen = screen
        self.muzzle = muzzle
        self.shooting = False
        self.drawFire = 0

    def draw(self, game):
        pass
        # insets = game.cameraHandler.getInsets()
        # if self.drawFire > 0:
            # pygame.draw.circle(self.screen, (255,10,10), [self.muzzle[X] + insets[X], self.muzzle[Y] + insets[Y]], 5, 1)

        # tmpPoints = []
        # for p in self.points:
        #     tmpPoints.append([p[X] + insets[X], p[Y] + insets[Y]])

        # pygame.draw.polygon(self.screen, self.color, tmpPoints, 1)


    def update(self, game):
        if self.shooting:            
            newBullet = bullet(self.muzzle[X], self.muzzle[Y], 2, self.direction, [0,0,0], 20, self.screen)
            game.objectHandler.createObject('bullet', newBullet)
            self.shooting = False

        if self.drawFire > 0:
            self.drawFire -= 1
        

    
    def move(self, xDis, yDis):
        self.anchor[X] += xDis
        self.anchor[Y] += yDis

        for point in self.points:
            point[X] += xDis
            point[Y] += yDis
        
        self.muzzle[X] += xDis
        self.muzzle[Y] += yDis 
    
    def setAnchor(self, newAnchor):
        anchorDif = [newAnchor[X] - self.anchor[X], newAnchor[Y] - self.anchor[Y]]

        for point in self.points:
            point[X] += anchorDif[X]
            point[Y] += anchorDif[Y]
        
        self.muzzle[X] += anchorDif[X]
        self.muzzle[Y] += anchorDif[Y]

        self.anchor = newAnchor        

    def setDirection(self, direction):
        dirDelta = direction - self.direction

        
        for point in self.points:
            point[X] -= self.anchor[X]
            point[Y] -= self.anchor[Y]

            xNew = point[X] * cos(dirDelta) - point[Y] * sin(dirDelta)
            yNew = point[X] * sin(dirDelta) + point[Y] * cos(dirDelta)


            point[X] = self.anchor[X] + xNew
            point[Y] = self.anchor[Y] + yNew

        self.muzzle[X] -= self.anchor[X]
        self.muzzle[Y] -= self.anchor[Y]

        xNew = self.muzzle[X] * cos(dirDelta) - self.muzzle[Y] * sin(dirDelta)
        yNew = self.muzzle[X] * sin(dirDelta) + self.muzzle[Y] * cos(dirDelta)


        self.muzzle[X] = self.anchor[X] + xNew
        self.muzzle[Y] = self.anchor[Y] + yNew
        

        self.direction = direction
    
    def shoot(self):
        self.shooting = True
        self.drawFire = 5


            
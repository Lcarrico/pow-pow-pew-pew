from pygame import Surface
import pygame
from shapely.geometry import Polygon
import math
import random
import utils

X = 0
Y = 1

class enemy():
    def __init__(self, x:int, y:int, radius:float, color:list, direction:float, speed:float, screen:Surface, health:float=100):
        self.x = x
        self.y = y
        self.radius = radius
        # Color is unused
        self.color = color
        self.direction = direction
        self.speed = speed
        self.screen = screen
        self.health = health
        self.image = pygame.image.load('wasp.png')
        self.image = pygame.transform.scale(self.image, [self.radius*4, self.radius*4])
    

    def draw(self, game):
        insets = game.cameraHandler.getInsets()
        tmpColorRed = max([round(self.health / 100 * 255), 0])
        # pygame.draw.circle(self.screen, (tmpColorRed, 0, 0), [self.x+insets[X], self.y+insets[Y]], self.radius)


        player1 = game.objectHandler.getObject('player', 0)
        newDir = math.atan2(player1.y - self.y, player1.x - self.x)

        tmpImage = pygame.transform.rotate(self.image, math.degrees(-newDir))
        new_rect = tmpImage.get_rect(center = self.image.get_rect(center = (300, 300)).center)
        new_rect.update(new_rect.left + self.x + insets[X] - 300, new_rect.top + self.y + insets[Y] - 300, new_rect.width, new_rect.height)

        game.screen.blit(tmpImage, new_rect)

    def move(self):
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)

    def update(self, game):
        self.move()
        player1 = game.objectHandler.getObject('player', 0)

        newDir = math.atan2(player1.y - self.y, player1.x - self.x)
        tolerance = random.randint(round(-math.pi*1/4 * 1000), round(math.pi*1/4 * 1000)) / 1000
        self.setDirection(newDir + tolerance)

        enemyCircle = {'radius':round(self.radius), 'x':round(self.x), 'y':round(self.y)}
        
        # Gun 1 bullets
        bullets = game.objectHandler.getObjectList('bullet').getAllObjects()

        bulletsToRemove = []
        for id, b in bullets.items():
            bulletCircle = {'radius':round(b.radius), 'x':round(b.x), 'y':round(b.y)}
            if utils.circleIntersectsCircle(enemyCircle, bulletCircle):
                self.takeDamage(18)
                bulletsToRemove.append(id)

        for id in bulletsToRemove:
            game.objectHandler.getObjectList('bullet').removeObject(id)


        playerCircle = {'radius':player1.radius, 'x':player1.x, 'y':player1.y}
        if utils.circleIntersectsCircle(playerCircle, enemyCircle):
            xDis = 10 * math.cos(newDir)
            yDis = 10 * math.sin(newDir)
            player1.move(game, xDis,yDis)
            player1.loseLife(1)


    def takeDamage(self, damage):
        self.health -= damage

    def setDirection(self, direction):
        self.direction = direction
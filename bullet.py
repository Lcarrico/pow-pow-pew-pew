from pygame import Surface
import pygame
import math
from shapely.geometry import Polygon

X=0
Y=1

class bullet():
    def __init__(self, x:int, y:int, radius:float, direction:float, color:list, speed:float, screen:Surface, disTraveled:float = 0):
        self.x = x
        self.y = y
        self.radius = radius
        self.direction = direction
        self.color = color
        self.screen = screen
        self.disTraveled = disTraveled
        self.speed = speed
    
    def draw(self, game):
        insets = game.cameraHandler.getInsets()
        pygame.draw.circle(self.screen, self.color, [self.x + insets[X], self.y + insets[Y]], self.radius)


    def update(self, game):
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)
        self.disTraveled += self.speed
    
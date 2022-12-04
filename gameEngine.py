import pygame
from player import player
from bullet import bullet
from enemy import enemy
from inputHandler import inputHandler  
from objectHandler import objectHandler
from levelHandler import levelHandler
from cameraHandler import cameraHandler
from worldHandler import worldHandler
from soundHandler import soundHandler
from screenHandler import screenHandler
import sys
from time import time
from math import pi
import utils
import math
import random

X=0
Y=1


class gameEngine():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width, self.height = self.screen.get_size()
        self.inputHandler = inputHandler(self)
        self.soundHandler = soundHandler(self)
        self.objectHandler = objectHandler(self)
        self.levelHandler = levelHandler(self)
        self.screenHandler = screenHandler(self)
        self.cameraHandler = cameraHandler(self)
        self.worldHandler = worldHandler(self)
        



    def instantiate(self):
        self.clock = pygame.time.Clock()
        player1 = player(1200, 1200, 8, [0,0,0], 0, 8, self.screen)
        self.objectHandler.createObject('player', player1)
        self.objectHandler.createObjectList('enemy')
        self.objectHandler.createObjectList('bullet')

        self.running = True

        # self.levelHandler.addEnemy()
        self.soundHandler.startMusic('Psycho Punch.wav')

    def update(self):
        self.inputHandler.update()
        self.screenHandler.update()

        if self.screenHandler.currentScreen == 'gameScreen':
            self.objectHandler.update()
            self.levelHandler.update()
        
        self.cameraHandler.update()
        self.soundHandler.update()
        


    def draw(self):

        # backgroundRect = pygame.Rect(0, 0, self.width, self.height)
        # pygame.draw.rect(self.screen,'black', backgroundRect)
        self.worldHandler.draw()

        self.objectHandler.draw()

        self.cameraHandler.draw()
        self.screenHandler.draw()

        pygame.display.flip()  # Refresh on-screen display
    
    def restart(self):

        player1 = player(1200, 1200, 8, [0,0,0], 0, 8, self.screen)
        self.objectHandler.getObjectList('player').setObject(0, player1)
        self.screenHandler.currentScreen = 'gameScreen'
        self.levelHandler.level = 0
        self.levelHandler.enemySpeed = 5

        self.objectHandler.getObjectList('bullet').wipe()
        self.objectHandler.getObjectList('enemy').wipe()




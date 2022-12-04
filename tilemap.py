import pygame
import numpy as np
import xmltodict
import csv
import math


X=0
Y=1
class tilemap:
    def __init__(self, tileset, size, screen, zoom=1):
        self.size = size
        self.tileset = tileset
        self.map = np.zeros(size, dtype=int)
        self.screen = screen
        self.zoom = zoom

    def draw(self, game):
        insets = game.cameraHandler.getInsets()
        player1 = game.objectHandler.getObject('player', 0)
        m, n = self.map.shape
        for i in range(m):
            for j in range(n):
                if self.map[i, j] != 0:
                    tile = self.tileset.tiles[self.map[i, j] - 1]
                    self.screen.blit(tile, (round(j*32*self.zoom + insets[X]), round(i*32*self.zoom +insets[Y])))

    def setZero(self):
        self.map = np.zeros(self.size, dtype=int)

    def setRandom(self):
        n = len(self.tileset.tiles)
        self.map = np.random.randint(n, size=self.size)
    
    def setMap(self, map):
        self.map = map

        

    def __str__(self):
        return f'{self.__class__.__name__} {self.size}'  
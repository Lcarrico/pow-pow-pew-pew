import pygame
from tileset import tileset
from tilemap import tilemap
import xmltodict
import numpy as np

X=0
Y=1

class worldHandler():
    def __init__(self, game, width=6400, height=6400, zoom=2):
        self.game = game
        self.width = width
        self.height = height
        self.zoom = zoom
        self.tileset = tileset('terrain_atlas.png', [32,32], 0, 0, zoom)
        self.tilemaps = []
        self.collisionGroups = []
        self.loadTMX(self.tileset, 'test2.tmx')


    def draw(self):

        insets = self.game.cameraHandler.getInsets()

        self.game.screen.blit(self.superMap, [insets[X], insets[Y]])

        # for collisionGroup in self.collisionGroups:
        #     for collision in collisionGroup:
        #         rect = pygame.Rect(collision['x'] + insets[X], collision['y']+ insets[Y], collision['width'], collision['height'])
        #         pygame.draw.rect(self.game.screen, 'blue', rect, 2)

    def loadTMX(self, tileset, filename):
        with open(filename, 'r') as f:
            xmlString = f.read()
        mapDict = xmltodict.parse(xmlString)

        count = 0
        for mapLayer in mapDict['map']['layer']:
            data = mapLayer['data']['#text']

            formattedData = []
            data = data.split(',\n')
            for line in data:
                line = line.split(',')
                formattedData.append(list(map(int, line)))
        
            dataMap = np.array(formattedData)
            newTilemap = tilemap(tileset, (round(self.width/32), round(self.height/32)), self.game.screen, self.zoom)
            newTilemap.setMap(dataMap)

            self.tilemaps.append(newTilemap)
            count += 1
        
        self.superMap = self.flattenTilemaps(self.tilemaps)

        
        for objectGroup in mapDict['map']['objectgroup']:

            collisionGroup = []
            
            for object in objectGroup['object']:
                if '@height' not in object.keys():
                    object['@height'] = object['@width']
                if '@width' not in object.keys():
                    object['@width'] = object['@height']
                rect = {'x':float(object['@x'])*self.zoom, 'y':float(object['@y'])*self.zoom, 
                    'width':float(object['@width'])*self.zoom, 'height':float(object['@height'])*self.zoom}
                collisionGroup.append(rect)

            self.collisionGroups.append(collisionGroup)

        
    def flattenTilemaps(self, tilemaps):
        superMap = pygame.Surface([self.width, self.height], pygame.SRCALPHA)

        for tilemap in tilemaps:
            m, n = tilemap.map.shape
            for i in range(m):
                for j in range(n):
                    if tilemap.map[i, j] != 0:
                        tile = tilemap.tileset.tiles[tilemap.map[i, j] - 1]
                        superMap.blit(tile, (round(j*32*self.zoom), round(i*32*self.zoom)))

        return superMap
            
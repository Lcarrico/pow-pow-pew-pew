import pygame

class tileset:
    def __init__(self, file, size=(32, 32), margin=1, spacing=1, zoom=1):
        self.file = file
        self.size = size
        self.margin = margin
        self.spacing = spacing
        self.zoom = zoom
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.tiles = []
        self.load()


    def load(self):

        self.tiles = []
        x0 = y0 = self.margin
        w, h = self.rect.size
        dx = self.size[0] + self.spacing
        dy = self.size[1] + self.spacing
        
        for y in range(y0, h, dy):
            for x in range(x0, w, dx):
                tile = pygame.Surface(self.size, pygame.SRCALPHA)
                tile.blit(self.image, (0, 0), (x, y, *self.size))
                scaledTile = pygame.transform.smoothscale(tile, (tile.get_width() * self.zoom, tile.get_height() * self.zoom))
                self.tiles.append(scaledTile)

    def __str__(self):
        return f'{self.__class__.__name__} file:{self.file} tile:{self.size}'
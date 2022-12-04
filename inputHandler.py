import pygame
import sys

class inputHandler():
    def __init__(self, game):
        self.game = game
    
    def update(self):
        if self.game.screenHandler.currentScreen == 'gameScreen':
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_a:
                        self.game.objectHandler.getObject('player', 0).startMovingLeft()
                    if event.key == pygame.K_s:
                        self.game.objectHandler.getObject('player', 0).startMovingDown()
                    if event.key == pygame.K_d:
                        self.game.objectHandler.getObject('player', 0).startMovingRight()
                    if event.key == pygame.K_w:
                        self.game.objectHandler.getObject('player', 0).startMovingUp()
                    if event.key == pygame.K_LSHIFT:
                        self.game.objectHandler.getObject('player', 0).startSprinting()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a: 
                        self.game.objectHandler.getObject('player', 0).stopMovingLeft()
                    if event.key == pygame.K_s:
                        self.game.objectHandler.getObject('player', 0).stopMovingDown()
                    if event.key == pygame.K_d:
                        self.game.objectHandler.getObject('player', 0).stopMovingRight()
                    if event.key == pygame.K_w:
                        self.game.objectHandler.getObject('player', 0).stopMovingUp()
                    if event.key == pygame.K_LSHIFT:
                        self.game.objectHandler.getObject('player', 0).stopSprinting()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.game.objectHandler.getObject('player', 0).startShooting(self.game)
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.game.objectHandler.getObject('player', 0).stopShooting(self.game)


        if self.game.screenHandler.currentScreen == 'startScreen':
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = pygame.mouse.get_pos()
                        if x > 800 and x < 300 + 800 and y > 525 and y < 150 + 525:
                            self.game.screenHandler.currentScreen = 'gameScreen'

        if self.game.screenHandler.currentScreen == 'gameOverScreen':
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_r:
                        self.game.restart()
                

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
import pygame

class screenHandler():
    def __init__(self, game):
        self.game = game
        self.screens = {}

        self.screens['startScreen'] = startScreen()
        self.screens['gameScreen'] = gameScreen()
        self.screens['gameOverScreen'] = gameOverScreen()

        self.currentScreen = 'startScreen'

    def update(self):
        self.screens[self.currentScreen].update(self.game)

    def draw(self):
        self.screens[self.currentScreen].draw(self.game)


class startScreen():
    def __init__(self):
        pass
    
    def update(self, game):
        pass

    def draw(self, game):
        # draw transparent background
        backgroundImage = pygame.Surface((game.width-600, game.height-400))
        backgroundImage.set_alpha(128)
        backgroundImage.fill((0,0,0))
        game.screen.blit(backgroundImage, (300,200))

        # adding text to screen
        my_font = pygame.font.SysFont('Comic Sans MS', 60)
        text_surface = my_font.render('POW POW PEW PEW', False, (255, 255, 255))
        game.screen.blit(text_surface, (650,350))


        x, y = pygame.mouse.get_pos()

        if x > 800 and x < 300 + 800 and y > 525 and y < 150 + 525:
            # add start image
            startImage = pygame.image.load("startButtonOnHover.png").convert_alpha()
            startImageScaled = pygame.transform.scale(startImage, (300, 300))
            game.screen.blit(startImageScaled, (800,450))
        else:
            # add start image
            startImage = pygame.image.load("startButton.png").convert_alpha()
            startImageScaled = pygame.transform.scale(startImage, (300, 300))
            game.screen.blit(startImageScaled, (800,450))


class gameScreen():
    def __init__(self):
        pass

    def update(self, game):
        pass

    def draw(self, game):
        player1 = game.objectHandler.getObject('player', 0)
        heartImage = pygame.image.load("0.bmp").convert_alpha()
        # startImageScaled = pygame.transform.scale(startImage, (300, 300))
        for i in range(player1.lives):
            game.screen.blit(heartImage, (10 + i * 50,10))

        playerKills = game.objectHandler.getObject('player', 0).kills

        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render(f'Score: {playerKills * 100}', False, (255, 255, 255))
        game.screen.blit(text_surface, (10,game.height - 50))

        highscore = game.levelHandler.highscore

        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render(f'Highscore: {highscore}', False, (255, 255, 255))
        game.screen.blit(text_surface, (10,game.height - 80))




class gameOverScreen():
    def __init__(self):
        pass

    def update(self, game):
        pass

    def draw(self, game):
        # draw transparent background
        backgroundImage = pygame.Surface((game.width-600, game.height-400))
        backgroundImage.set_alpha(128)
        backgroundImage.fill((0,0,0))
        game.screen.blit(backgroundImage, (300,200))

        # adding text to screen
        my_font = pygame.font.SysFont('Comic Sans MS', 60)
        text_surface = my_font.render('GAME OVER', False, (255, 255, 255))
        game.screen.blit(text_surface, (775,350))

        my_font = pygame.font.SysFont('Comic Sans MS' , 30)
        text_surface = my_font.render('Press \'r\' to restart', False, (255, 255, 255))
        game.screen.blit(text_surface, (630,550))

        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render('Press \'esc\' to exit', False, (255, 255, 255))
        game.screen.blit(text_surface, (1030,550))

        playerKills = game.objectHandler.getObject('player', 0).kills

        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render(f'Score: {playerKills * 100}', False, (255, 255, 255))
        game.screen.blit(text_surface, (10,game.height - 50))

X = 0
Y = 1

class cameraHandler():
    def __init__(self, game):
        self.game = game
        self.insets = [0,0]
        self.width = game.width
        self.height = game.height

    def getInsets(self):
        return [round(self.insets[X]), round(self.insets[Y])]
    
    def move(self, dx, dy):
        self.insets[X] -= dx
        self.insets[Y] -= dy
    
    def set(self, x, y):
        dx = round(x - self.width/2 + self.insets[X])
        dy = round(y - self.height/2 + self.insets[Y])
        self.move(dx, dy)
    
    def update(self):
        p0 = self.game.objectHandler.getObject('player', 0)
        self.set(p0.x, p0.y)
    
    def draw(self):
        pass

    
    

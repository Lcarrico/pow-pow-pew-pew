import random
from enemy import enemy
import math
import utils

class levelHandler():
    def __init__(self, game, level:int=0):
        self.game = game
        self.level = level
        self.enemySpeed = 5

        with open('highscore.txt', 'r') as infile:
            highscore = int(infile.read())
        self.highscore = highscore
    
    def update(self):

        self.handlePlayerLogic()
        self.handleEnemyLogic()
        self.handleBulletLogic()

        playerScore = self.game.objectHandler.getObject('player', 0).kills * 100

        if playerScore > self.highscore:
            self.highscore = playerScore


    def handlePlayerLogic(self):
        # if player has no health, end game
        if self.game.objectHandler.getObject('player', 0).lives <= 0:
            self.game.screenHandler.currentScreen = 'gameOverScreen'

            with open('highscore.txt', 'w') as outfile:
                outfile.write(str(self.highscore))


    def handleEnemyLogic(self):


        # start with 10 and every round add 15
        if len(self.game.objectHandler.getObjectList('enemy').getAllObjects().keys()) <= 0:
            self.levelup()

        # if enemy has no health, remove enemy
        enemyObjectList = self.game.objectHandler.getObjectList('enemy')
        enemies = enemyObjectList.getAllObjects()
        toRemove = []
        for i, e in enemies.items():
            if e.health < 0:
                toRemove.append(i)
                self.game.objectHandler.getObject('player', 0).kills += 1
        enemyObjectList.removeObjects(toRemove)

    def handleBulletLogic(self):
        bulletObjectList = self.game.objectHandler.getObjectList('bullet')
        bullets = bulletObjectList.getAllObjects()
        toRemove = []
        for i, b in bullets.items():
            if b.disTraveled > 2500:
                toRemove.append(i)
            else:
                walls = self.game.worldHandler.collisionGroups[1]
                for wall in walls:
                    rect = {'x':wall['x']+wall['width']/2, 'y':wall['y']+wall['height']/2, 'width':wall['width'], 'height':wall['height']}
                    circ = {'x':b.x, 'y':b.y, 'radius':b.radius}
                    if utils.circleIntersectsRectangle(circ,rect):
                        print('intersecting')
                        toRemove.append(i)
        bulletObjectList.removeObjects(toRemove)

    def addEnemy(self):
        xPos = random.randint(-500, self.game.width + 500)
        while xPos >= 0 and xPos <= self.game.width:
            xPos = random.randint(-500, self.game.width + 500)


        yPos = random.randint(-500, self.game.height + 500)
        while yPos >= 0 and yPos <= self.game.height:
             yPos = random.randint(-500, self.game.height + 500)

        e1 = enemy(xPos, yPos, 20, (0,0,0), 0, self.enemySpeed, self.game.screen)
        self.game.objectHandler.createObject('enemy', e1)
    
    def levelup(self):
        self.level += 1

        self.enemySpeed += 0.3
        f = lambda x: round(10 * math.log(x) + 5)
        for i in range(f(self.level)):
            self.addEnemy()

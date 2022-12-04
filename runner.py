from gameEngine import gameEngine


game = gameEngine()
game.instantiate()


while game.running:

    game.update()
    game.draw()
    game.clock.tick(60)
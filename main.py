import game

game = game.Enduro()
for i_episode in range(20):
    game.reset()
    for t in range(1000):
        game.run()
        if game.isDone:
            break
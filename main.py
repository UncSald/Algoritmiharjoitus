import src.game


# DEFINE MAIN FUNCTION
def main():

        decision = str(input('Type "demo" to see demo, "game" to play the game, anything else exits: '))
        
        if decision == 'demo':
            pass

        elif decision == 'game':
            # DEFINE WIDTH, HEIGHT, AND TILE SIZE.
            # FEEL FREE TO CHANGE THESE AND SEE HOW THE MAP GENERATES
            WIDTH = 1500
            HEIGHT = 1000
            tile_size = 32

            new_game = src.game.Game(WIDTH,HEIGHT,tile_size)

            new_game.run()
        else:
            print("bye bye")


if __name__ == "__main__":
    main()

import sys
import pygame
import src.game


# DEFINE MAIN FUNCTION
def main():

    # DEFINE WIDTH, HEIGHT, AND TILE SIZE.
    # FEEL FREE TO CHANGE THESE AND SEE HOW THE MAP GENERATES
    WIDTH = 1500
    HEIGHT = 1000
    tile_size = 32

    new_game = src.game.Game(WIDTH,HEIGHT,tile_size)

    new_game.run()



if __name__ == "__main__":
    main()

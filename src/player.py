"""Module contains the player class which is used
to hold information of a player in the game.
"""
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, width :int, height :int,\
                 render_point :tuple[int,int]):
        """Class constructor generates a new player.

        Args:
            width (int): tilesize of the game
            height (int): tilesize of the game
        """
        pygame.sprite.Sprite.__init__(self)
        self.image_up = pygame.image.load('src/assets/dude.png')
        self.image_down = pygame.image.load('src/assets/dude_down.png')
        self.image_left = pygame.image.load('src/assets/dude_left.png')
        self.image_right = pygame.image.load('src/assets/dude_right.png')
        self.image_up = pygame.transform.scale(self.image_up,(width,height))
        self.image_down = pygame.transform.scale(self.image_down,(width,height))
        self.image_left = pygame.transform.scale(self.image_left,(width,height))
        self.image_right = pygame.transform.scale(self.image_right,(width,height))
        self.image = self.image_up
        self.rect = self.image.get_rect(topleft=render_point)
        self.x, self.y = render_point
        self.velocity = width/8
        self.changes_x = 0
        self.changes_y = 0
        self.clear = False
        self.items = []
        self.held_items = []

"""Module contains the GameTile class and the Item class.
These are object classes for the game. 
"""

import pygame

class GameTile(pygame.sprite.Sprite):
    """ GameTile class holds information of game tiles such as,
    sprite and location.
    Args:
        pygame (sprite.Sprite): Super class
    """
    def __init__(self, tile_size:int,\
                 render_point :tuple[int,int],val):
        """Class constructor for GameTile sprite.

        Args:
            tile_size (int): Tile size of the game.
        """
        pygame.sprite.Sprite.__init__(self)
        self.name :str
        if val in (1,2):
            self.image = pygame.image.load('src/assets/floor_2.png')
            self.name = 'floor'
        elif val==3:
            self.image = pygame.image.load('src/assets/prev_door.png')
            self.name = 'start door'
        elif val==4:
            self.image = pygame.image.load('src/assets/next_door.png')
            self.name = 'next door'
        elif val == 5:
            self.image = pygame.image.load('src/assets/wall.png')
            self.name = 'near wall'
        else:
            self.image = pygame.image.load('src/assets/floor.png')
            self.name = 'far wall'
        self.image = pygame.transform.scale(self.image,(tile_size,tile_size))
        self.rect = self.image.get_rect(topleft=render_point)
        self.x, self.y = render_point


    def update(self, player):
        """Update function to have the objects move around the player.

        Args:
            player (Player): Player used for the update function.
        """
        self.x = self.x - player.changes_x
        self.y = self.y - player.changes_y
        self.rect.topleft=(self.x,self.y)

    def __repr__(self):
        return f"{self.name}"

class Item(pygame.sprite.Sprite):
    """Class constructor for Item sprite.

    Args:
        pygame (sprite.Sprite): Super class
    """
    def __init__(self,tile_size:int,render_point :tuple[int,int], image, name:str):
        """Class constructor for Item sprite.

        Args:
            tile_size (int): Tile size of the game.
            render_point (tuple[int,int]): Point of origin for the sprite center.
            image (pygame.image): Image used for item creation.
            name (str): Name for the item.
        """
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = image
        self.image = pygame.transform.scale(self.image,(tile_size,tile_size))
        self.rect = self.image.get_rect(topleft=render_point)
        self.x, self.y = render_point

    def update(self, player):
        """Update function to have the objects move around the player.

        Args:
            player (Player): Player used for the update function.
        """
        self.x = self.x - player.changes_x
        self.y = self.y - player.changes_y
        self.rect.topleft=(self.x,self.y)

    def __repr__(self):
        return f"{self.name.replace('_', ' ')}"

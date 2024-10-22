import pygame




class Wall(pygame.sprite.Sprite):
    """

    Args:
        pygame (sprite.Sprite): Super class
    """
    def __init__(self, tile_size:int,\
                 render_point :tuple[int,int]):
        """Class constructor for Wall sprite.

        Args:
            tile_size (int): Tile size of the game.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('src/assets/wall.png')
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




class Floor(pygame.sprite.Sprite):
    """Class constructor for Floor sprite.

    Args:
        pygame (sprite.Sprite): Super class
    """
    def __init__(self, tile_size:int,\
                 render_point :tuple[int,int]):
        """Class constructor for Floor sprite.

        Args:
            tile_size (int): Tile size of the game.
        """
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('src/assets/floor.png')
        self.image = pygame.transform.scale(self.image,(tile_size,tile_size))

        self.rect = self.image.get_rect()
        self.x, self.y = render_point
    
    def update(self, player):
        """Update function to have the objects move around the player.

        Args:
            player (Player): Player used for the update function.
        """
        self.x = self.x - player.changes_x
        self.y = self.y - player.changes_y
        self.rect.topleft=(self.x,self.y)




class Door(pygame.sprite.Sprite):
    """Class constructor for Door sprite.

    Args:
        pygame (sprite.Sprite): Super class
    """
    def __init__(self, tile_size:int,\
                 render_point :tuple[int,int], value):
        """Class constructor for Door sprite.

        Args:
            tile_size (int): Tile size of the game.
            value (_type_): Defines the image used in rendering. 3 Is the start point, 4 is the goal point.
        """
        pygame.sprite.Sprite.__init__(self)
        if value == 3:
            self.image = pygame.image.load('src/assets/prev_door.png')
        if value == 4:
            self.image = pygame.image.load('src/assets/next_door.png')
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




class Item(pygame.sprite.Sprite):
    """Class constructor for Item sprite.

    Args:
        pygame (sprite.Sprite): Super class
    """
    def __init__(self,tile_size,render_point :tuple[int,int], image, name):
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
        self.rect = self.image.get_rect(center=render_point)
        self.x, self.y = render_point

    def update(self, player):
        """Update function to have the objects move around the player.

        Args:
            player (Player): Player used for the update function.
        """
        self.x = self.x - player.changes_x
        self.y = self.y - player.changes_y
        self.rect.topleft=(self.x,self.y)

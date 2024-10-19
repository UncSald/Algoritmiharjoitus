import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, width :int, height :int,\
                 render_point :tuple[int,int], walls :pygame.sprite.Group, goal :pygame.sprite.Sprite):
        """Class constructor generates a new player.

        Args:
            width (int): tilesize of the game
            height (int): tilesize of the game
            walls (pygame.sprite.Group): _description_
            goal (pygame.sprite.Sprite): _description_
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('src/assets/dude.png')
        self.image_up = pygame.image.load('src/assets/dude.png')
        self.image_down = pygame.image.load('src/assets/dude_down.png')
        self.image_left = pygame.image.load('src/assets/dude_left.png')
        self.image_right = pygame.image.load('src/assets/dude_right.png')
        self.rect = self.image.get_rect(topleft=render_point)
        self.x, self.y = render_point
        self.x_velocity = width/8
        self.y_velocity = height/8
        self.walls = walls
        self.changes_x = 0
        self.changes_y = 0
        self.goal = goal
        self.clear = False

import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, width :int, height :int,\
                 render_point :tuple[int,int]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('src/assets/wall.png')
        self.rect = self.image.get_rect(topleft=render_point)
        self.x, self.y = render_point

    def update(self, player):
        self.x = self.x - player.changes_x
        self.y = self.y - player.changes_y
        self.rect.topleft=(self.x,self.y)




class Floor(pygame.sprite.Sprite):
    def __init__(self, width :int, height :int,\
                 render_point :tuple[int,int], value):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('src/assets/floor_2.png')

        self.rect = self.image.get_rect()
        self.x, self.y = render_point
    
    def update(self, player):
        self.x = self.x - player.changes_x
        self.y = self.y - player.changes_y
        self.rect.topleft=(self.x,self.y)




class Door(pygame.sprite.Sprite):
    def __init__(self, width :int, height :int,\
                 render_point :tuple[int,int], value):
        pygame.sprite.Sprite.__init__(self)
        if value == 3:
            self.image = pygame.image.load('src/assets/prev_door.png')
        if value == 4:
            self.image = pygame.image.load('src/assets/next_door.png')
        self.rect = self.image.get_rect(topleft=render_point)
        self.x, self.y = render_point

    def update(self, player):
        self.x = self.x - player.changes_x
        self.y = self.y - player.changes_y
        self.rect.topleft=(self.x,self.y)

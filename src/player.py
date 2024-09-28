import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, width :int, height :int,\
                 render_point :tuple[int,int], walls :pygame.sprite.Group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill('pink')
        self.rect = self.image.get_rect(topleft=render_point)
        self.x, self.y = render_point
        self.x_velocity = width/8
        self.y_velocity = height/8
        self.walls = walls

    def collision(self, group :pygame.sprite.Group):
        pass

    def update(self):
        pass

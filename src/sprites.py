import pygame



class Wall(pygame.sprite.Sprite):
    def __init__(self, width :int, height :int,\
                 render_point :tuple[int,int]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill('white')
        self.rect = self.image.get_rect(topleft=render_point)
        self.x, self.y = render_point

    def update(self, player):
        self.x = self.x - player.changes_x
        self.y = self.y - player.changes_y
        self.rect.topleft=(self.x,self.y)


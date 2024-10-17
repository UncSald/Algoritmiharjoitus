import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, width :int, height :int,\
                 render_point :tuple[int,int], walls :pygame.sprite.Group):
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

    def collision(self, group :pygame.sprite.Group):
        for sprite in group.sprites():    
            if pygame.sprite.collide_rect(self, sprite):
                if self.rect.bottom >= sprite.rect.top and self.rect.bottom < sprite.rect.bottom:
                    self.changes_y -= self.y_velocity
                if self.rect.top <= sprite.rect.bottom and self.rect.top > sprite.rect.top:
                    self.changes_y += self.y_velocity
                if self.rect.left <= sprite.rect.right and self.rect.left > sprite.rect.left:
                    self.changes_x += self.x_velocity
                if self.rect.right >= sprite.rect.left and self.rect.right < sprite.rect.right:
                    self.changes_x -= self.x_velocity

    def update(self):
        self.changes_x = 0
        self.changes_y = 0
        self.collision(self.walls)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.changes_x -= self.x_velocity
            self.image = self.image_left
        elif keys[pygame.K_d]:
            self.changes_x += self.x_velocity
            self.image = self.image_right
        elif keys[pygame.K_w]:
            self.changes_y -= self.y_velocity
            self.image = self.image_up
        elif keys[pygame.K_s]:
            self.changes_y += self.y_velocity
            self.image = self.image_down
        self.rect.topleft=(self.x,self.y)

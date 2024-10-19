import sys
import pygame
import pygame.gfxdraw
from src.bowyerWatson import BowyerWatson
from src.roomGeneration import generate_rooms, start_end
from src.listMatrix import list_to_matrix,point_to_coord
from src.kruskal import kruskal
from src.a_star import build_path
from src.player import Player
from src.create_objects import create_objects

class Game:
    def __init__(self,widht,height,tile):
        # INIT PYGAME
        pygame.init()
        self.running = True
        self.widht = widht
        self.height = height
        self.tile_size = tile
        self.font = pygame.font.SysFont('Arial', 25)
        

        self.final_level = 1
        self.level_num = 0

    def run(self):

        # ADD BACKGROUND COLOR, FEEL FREE TO CHANGE IT
        BG = pygame.Surface((self.widht,self.height))
        BG.fill((20,49,30))

        # DEFINE SCREEN SIZE AND self.height
        # SCREEN SIZE CAN BE CHANGED BUT SHOULD YOU CHANGE IT
        # REMEMBER TO CHANGE THE PLAYER POSITION, AND
        # CHANGES_X/Y ACCORDINGLY
        screen = pygame.display.set_mode((self.widht/2,self.height/2))
        menu = pygame.surface.Surface((self.widht/2-200,self.height/2-200))
        menu.fill((200,255,255,0))
        font = pygame.font.SysFont('Arial', 30, bold=True)
        
        # CREATE LEVEL
        self.create_level()
        self.level_num += 1
        self.yes_no = False

        # DEFINE CLOCK FOR SMOOTH SAILING
        clock = pygame.time.Clock()

        # MAIN LOOP
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # DEFINE KEYS
            keys = pygame.key.get_pressed()
            
            # DRAW ALL SPRITES IN GROUPS
            if self.yes_no is not True:
                screen.blit(BG, (0,0))
                for sprite in self.walls:
                    screen.blit(sprite.image,(sprite.x,sprite.y))
                    sprite.update(self.player1)
                for sprite in self.floor:
                    screen.blit(sprite.image,(sprite.x, sprite.y))
                    sprite.update(self.player1)
                for sprite in self.doors:
                    screen.blit(sprite.image,(sprite.x, sprite.y))
                    sprite.update(self.player1)                
                for sprite in self.player_group:
                    screen.blit(sprite.image,(sprite.x, sprite.y))
                    # UPDATE PLAYER
                if self.player1.clear is not True:
                    self.player_upate()
                else:
                    self.yes_no = True
                
            
            else:
                if self.level_num == self.final_level:
                    screen.blit(menu,(100,100))
                    screen.blit(font.render('YOU WIN !', True, (255, 0, 255)),(200,200))
                else:
                    screen.blit(menu,(100,100))
                    screen.blit(font.render('Press space to continue', True, (190, 0, 0)),(200,200))
                    
                    if keys[pygame.K_SPACE]:
                        self.player1.changes_x = 0
                        self.player1.changes_y = 0
                        self.level_num += 1
                        self.create_level()
            
            screen.blit(font.render(f'B{self.level_num}f', True, (250, 0, 100)),(10,10))
            clock.tick(60)
            pygame.display.flip()

    def create_level(self):

        # GENERATE ROOMS AND TAKE THEIR COORDINATES AND CENTER POINTS
        rooms_gened = generate_rooms(20 ,self.widht, self.height, self.tile_size)
        rooms, centers = rooms_gened
        print(f"rooms done")

        # INIT AND RUN BOWYER-WATSON -ALGORITHM
        # AS INPUT GIVE IT THE ROOM CENTERS, AND SCREEN SIZE
        rp_alg = BowyerWatson(centers, self.widht, self.height)
        rp_alg.run()
        print(f"rp_alg done")

        # DEFINE STARTPOINT AND ENDPOINT
        start_point, self.end_point = start_end(centers, rp_alg._all_edges)
        print(point_to_coord(start_point,self.tile_size))
        print(point_to_coord((start_point[0]-self.widht/4,start_point[1]-self.height/4),self.tile_size))

        # DEFINE GROUPS FOR WALLS, FLOOR, DOOR, AND PLAYER
        self.walls = pygame.sprite.Group()
        self.floor = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()

        # DEFINE PLAYER AND START POINT FOR CORRECT MAP POSITION
        self.player1 = Player(self.tile_size/2,self.tile_size/2,(self.widht/4,self.height/4), self.walls, self.doors)
        self.player1.add(self.player_group)

        self.player1.changes_x = start_point[0]-self.widht/4
        self.player1.changes_y = start_point[1]-self.height/4

        # CREATE MAP CONTAINING ROOMS, START, AND GOAL
        temporary_map = list_to_matrix(rooms,centers,self.widht, self.height,\
                            start_point, self.end_point, self.tile_size)
        print(f"map done, {len(temporary_map[0])}x{len(temporary_map)} tiles")

        # CREATE MINIMUM SPANNING TREE FROM EDGES IN TRIANGULATION
        mst = kruskal(rp_alg._all_edges, start_point)
        print(f"kruskal done")

        # CREATE FINAL MAP FROM TEMPORARY ONE
        # THIS TIME IT CONTAINS PATHS BETWEEN ROOMS CREATED
        # BY A_STAR
        MAP = build_path(temporary_map,mst,self.tile_size)
        print(f"final map done")

        create_objects(MAP, self.tile_size, self.floor, self.walls, self.doors)
        print(f"create objects done")
        self.yes_no = False

    def player_collision(self):
        for sprite in self.walls:    
            if pygame.sprite.collide_rect(self.player1, sprite):
                if self.player1.rect.bottom >= sprite.rect.top and\
                      self.player1.rect.bottom < sprite.rect.bottom:
                    self.player1.changes_y -= self.player1.y_velocity
                if self.player1.rect.top <= sprite.rect.bottom and\
                      self.player1.rect.top > sprite.rect.top:
                    self.player1.changes_y += self.player1.y_velocity
                if self.player1.rect.left <= sprite.rect.right and\
                      self.player1.rect.left > sprite.rect.left:
                    self.player1.changes_x += self.player1.x_velocity
                if self.player1.rect.right >= sprite.rect.left and\
                      self.player1.rect.right < sprite.rect.right:
                    self.player1.changes_x -= self.player1.x_velocity

        for door in self.doors:
            if pygame.sprite.collide_rect(self.player1,door):
                self.player1.changes_x = 0
                self.player1.changes_y = 0
                self.player1.clear = True
    
    def player_upate(self):
            self.player1.changes_x = 0
            self.player1.changes_y = 0
            # self.collision(self.walls)
            self.player_collision()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and keys[pygame.K_w]:
                self.player1.changes_x -= self.player1.x_velocity/2
                self.player1.changes_y -= self.player1.y_velocity/2
                self.player1.image = self.player1.image_left
            
            elif keys[pygame.K_a] and keys[pygame.K_s]:
                self.player1.changes_x -= self.player1.x_velocity/2
                self.player1.changes_y += self.player1.y_velocity/2
                self.player1.image = self.player1.image_left
            elif keys[pygame.K_d] and keys[pygame.K_w]:
                self.player1.changes_x += self.player1.x_velocity/2
                self.player1.changes_y -= self.player1.y_velocity/2
                self.player1.image = self.player1.image_right

            elif keys[pygame.K_d] and keys[pygame.K_s]:
                self.player1.changes_x += self.player1.x_velocity/2
                self.player1.changes_y += self.player1.y_velocity/2
                self.player1.image = self.player1.image_right

            elif keys[pygame.K_a]:
                self.player1.changes_x -= self.player1.x_velocity
                self.player1.image = self.player1.image_left
            elif keys[pygame.K_d]:
                self.player1.changes_x += self.player1.x_velocity
                self.player1.image = self.player1.image_right
            elif keys[pygame.K_w]:
                self.player1.changes_y -= self.player1.y_velocity
                self.player1.image = self.player1.image_up
            elif keys[pygame.K_s]:
                self.player1.changes_y += self.player1.y_velocity
                self.player1.image = self.player1.image_down
            self.player1.rect.topleft=(self.player1.x,self.player1.y)
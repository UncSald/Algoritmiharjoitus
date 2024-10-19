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
from src.sprites import Item

class Game:
    def __init__(self,widht,height,tile):
        # INIT PYGAME
        pygame.init()
        self.running = True
        self.widht = widht
        self.height = height
        self.tile_size = tile
        self.font = pygame.font.SysFont('Arial', 20)
        self.items = ['key']
        self.key = pygame.image.load('src/assets/key.png')

        self.has_key = False
        self.collect_item = False
        self.door_cooldown = False
        self.final_level = 2
        self.level_num = 0

        # DEFINE GROUPS FOR WALLS, FLOOR, DOOR, AND PLAYER
        self.walls = pygame.sprite.Group()
        self.floor = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.item_group = pygame.sprite.Group()




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
        self.action = False

        # DEFINE CLOCK FOR SMOOTH SAILING
        clock = pygame.time.Clock()
        cooldown = 5
        count_to_exit = 6

        # MAIN LOOP
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # DEFINE KEYS
            keys = pygame.key.get_pressed()
            
            # DRAW ALL SPRITES IN GROUPS
            if self.action is not True:
                if self.door_cooldown is True:
                    cooldown -= 1/60
                    if cooldown <= 0:
                        self.door_cooldown = False
                        cooldown = 5
                screen.blit(BG, (0,0))
                for sprite in self.walls.sprites():
                    screen.blit(sprite.image,(sprite.x,sprite.y))
                    sprite.update(self.player1)
                for sprite in self.floor.sprites():
                    screen.blit(sprite.image,(sprite.x, sprite.y))
                    sprite.update(self.player1)
                for sprite in self.doors.sprites():
                    screen.blit(sprite.image,(sprite.x, sprite.y))
                    sprite.update(self.player1)
                for item in self.item_group.sprites():
                    screen.blit(item.image,(item.x,item.y))
                    item.update(self.player1)
                for sprite in self.player_group.sprites():
                    screen.blit(sprite.image,(sprite.x, sprite.y))
                    # UPDATE PLAYER
                if self.player1.clear is not True:
                    self.player_upate()
                else:
                    self.action = True
                
            elif self.action is True and self.collect_item is True:
                    screen.blit(menu,(100,100))
                    screen.blit(font.render('Press space to collect item', True, (255, 0, 255)),(200,250))
                    screen.blit(font.render(f'You have found a {self.collectable_item.name}', True, (255, 0, 255)),(200,200))
                    if keys[pygame.K_SPACE]:
                        if self.collectable_item.name == 'key':
                            self.item_group.remove(self.collectable_item)
                            self.has_key = True
                        self.action=False
                        self.collect_item = False
            
            elif self.has_key is True and self.door_cooldown is False:
                if self.level_num == self.final_level:
                    screen.blit(menu,(100,100))
                    screen.blit(font.render('YOU WIN !', True, (255, 0, 255)),(300,200))
                    screen.blit(font.render(f'exit in {int(count_to_exit)}', True, (255, 0, 255)),(310,300))
                    count_to_exit -= 1/60
                    if count_to_exit <= 1:
                        pygame.quit()
                        sys.exit()

                else:
                    screen.blit(menu,(100,100))
                    screen.blit(font.render('Press space to open door', True, (190, 0, 0)),(200,200))
                    
                    if keys[pygame.K_SPACE]:
                        self.has_key = False
                        self.level_num += 1
                        self.create_level()

            elif self.door_cooldown is False:
                screen.blit(menu,(100,100))
                screen.blit(font.render('The door seems to require a key...', True, (190, 0, 0)),(180,200))
                screen.blit(font.render('Press space to continue', True, (190, 0, 0)),(200,250))
                if keys[pygame.K_SPACE]:
                    self.player1.clear = False
                    self.action = False
                    self.door_cooldown = True
            else:
                if keys[pygame.K_SPACE]:
                    self.player1.clear = False
                    self.action = False

            
            screen.blit(font.render(f'B{self.level_num}f', True, (250, 0, 100)),(10,10))
            clock.tick(60)
            pygame.display.flip()




    def create_level(self):

        # CLEAR SPRITE GROUPS
        self.walls.empty()
        self.floor.empty()
        self.player_group.empty()
        self.doors.empty()
        self.item_group.empty()

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
        start_point, end_point, self.key_location = start_end(centers, rp_alg._all_edges)

        # DEFINE PLAYER AND START POINT FOR CORRECT MAP POSITION
        self.player1 = Player(self.tile_size/2,self.tile_size/2,(self.widht/4,self.height/4), self.walls, self.doors)
        self.player1.add(self.player_group)

        self.player1.changes_x = start_point[0]-self.widht/4
        self.player1.changes_y = start_point[1]-self.height/4

        # CREATE MAP CONTAINING ROOMS, START, AND GOAL
        temporary_map = list_to_matrix(rooms,centers,self.widht, self.height,\
                            start_point, end_point, self.tile_size)
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
        self.create_items()
        print(f"create objects done")
        self.action = False




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
            if pygame.sprite.collide_rect(self.player1,door) and self.door_cooldown is False:
                self.player1.clear = True
        
        for item in self.item_group:
            if pygame.sprite.collide_rect(self.player1,item):
                self.collectable_item = item
                self.collect_item = True
                self.action = True
    



    def player_upate(self):
            self.player1.changes_x = 0
            self.player1.changes_y = 0
            # self.collision(self.walls)
            self.player_collision()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and keys[pygame.K_w]:
                self.player1.changes_x -= self.player1.x_velocity/1.6
                self.player1.changes_y -= self.player1.y_velocity/1.6
                self.player1.image = self.player1.image_left
            elif keys[pygame.K_a] and keys[pygame.K_s]:
                self.player1.changes_x -= self.player1.x_velocity/1.6
                self.player1.changes_y += self.player1.y_velocity/1.6
                self.player1.image = self.player1.image_left
            elif keys[pygame.K_d] and keys[pygame.K_w]:
                self.player1.changes_x += self.player1.x_velocity/1.6
                self.player1.changes_y -= self.player1.y_velocity/1.6
                self.player1.image = self.player1.image_right
            elif keys[pygame.K_d] and keys[pygame.K_s]:
                self.player1.changes_x += self.player1.x_velocity/1.6
                self.player1.changes_y += self.player1.y_velocity/1.6
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



    def create_items(self):
        for item in self.items:
            if item == 'key':
                key = Item((self.key_location),self.key, 'key')
                self.item_group.add(key)

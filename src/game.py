import sys
import pygame
import pygame.gfxdraw
from src.bowyerWatson import BowyerWatson
from src.roomGeneration import generate_rooms, start_end
from src.listMatrix import list_to_matrix
from src.kruskal import kruskal
from src.a_star import build_path
from src.player import Player
from src.create_objects import create_objects
from src.sprites import Item

class Game:
    """Class for holding data for a dungeon exploring game.
    """

    def __init__(self,width,height):
        """Class constructor for Game.

        Args:
            width (_type_): Game screen width, used for screen size.
            height (_type_): Game screen height, used for screen size
        """

        pygame.init()
        self.running = True
        self.widht = width
        self.height = height
        self.tile_size = 32
        
        self.items = {}
        self.items['key'] = pygame.image.load('src/assets/key.png')

        self.has_key = False
        self.collect_item = False
        self.door_cooldown = False
        self.action = False

        self.final_level = 2
        self.level_num = 0
    
    def run(self):
        """Run method is used to start the game.
        Many pygame objects are defined in the run function.
        Calls handler functions and handles some game events
        itself.
        """

        screen = pygame.display.set_mode((self.widht/2,self.height/2))
        background = pygame.Surface((self.widht,self.height))
        background.fill((20,49,30))
        menu = pygame.surface.Surface((self.widht/2-200,self.height/2-200))
        menu.fill((200,255,255,0))
        font = pygame.font.SysFont('Arial', 25, bold=True)
        clock = pygame.time.Clock()
        self.walls = pygame.sprite.Group()
        self.floor = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.item_group = pygame.sprite.Group()
        
        self.create_level()

        cooldown = 5
        count_to_exit = 6

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("bye bye")
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            
            if self.action is not True:
                if self.door_cooldown is True:
                    cooldown -= 1/60
                    if cooldown <= 0:
                        self.door_cooldown = False
                        cooldown = 5

                screen.blit(background, (0,0))
                
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

                if self.player1.clear is not True:
                    self.player_update()
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
                        print("Congratulations!")
                        pygame.quit()
                        sys.exit()

                else:
                    screen.blit(menu,(100,100))
                    screen.blit(font.render('Press space to open door', True, (190, 0, 0)),(200,200))
                    
                    if keys[pygame.K_SPACE]:
                        self.has_key = False
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
        """Creates a level using multiple modules, such as:
        the bowyer-watson algorithm, roomGeneration, listMatrix,
        kruskal -algorithm, A* -algorithm, and create_objects.
        All these functions together form a randomly generated dungeon
        with some dead ends and a random start and end point.
        """

        self.walls.empty()
        self.floor.empty()
        self.player_group.empty()
        self.doors.empty()
        self.item_group.empty()

        rooms_gened = generate_rooms(20 ,self.widht, self.height, self.tile_size)
        rooms, centers = rooms_gened

        rp_alg = BowyerWatson(centers, self.widht, self.height)
        rp_alg.run()

        start_point, end_point, self.key_location = start_end(centers, rp_alg._all_edges)

        self.player1 = Player(self.tile_size/2,self.tile_size/2,\
                              (self.widht/4,self.height/4), self.walls, self.doors)
        self.player1.add(self.player_group)

        temporary_map = list_to_matrix(rooms,centers,self.widht, self.height,\
                            start_point, end_point, self.tile_size)

        mst = kruskal(rp_alg._all_edges, start_point)

        MAP = build_path(temporary_map,mst,self.tile_size)

        create_objects(MAP, self.tile_size, self.floor, self.walls, self.doors)
        self.create_items()

        self.player1.changes_x = start_point[0]-self.widht/4
        self.player1.changes_y = start_point[1]-self.height/4
        
        self.action = False
        self.level_num += 1



    def player_collision(self):
        """Handler for player collisions.
        Player collisions act as triggers in the game in certain situations.
        """

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
    



    def player_update(self):
        """Player update function.
        Handles map movement to create illusion of player moving.
        """

        self.player1.changes_x = 0
        self.player1.changes_y = 0
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




    def create_items(self):
        """Creates items from given item dictionary.
        """

        for item in self.items.keys():
            if item == 'key':
                key = Item((self.key_location),self.items['key'], 'key')
                self.item_group.add(key)

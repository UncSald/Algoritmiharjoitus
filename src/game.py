import sys
import pygame
import pygame.gfxdraw
from src.bowyer_watson import BowyerWatson
from src.room_generation import generate_rooms, start_end
from src.list_matrix import list_to_matrix, closest_walls
from src.kruskal import kruskal
from src.a_star import build_path
from src.player import Player
from src.create_objects import create_objects
from src.sprites import Item
from src.game_settings import *




class Game:
    """Class for holding data for a dungeon exploring game.
    """

    def __init__(self,width,height):
        """Class constructor for Game.

        Args:
            width (int): Game self.screen width, used for self.screen size.
            height (int): Game self.screen height, used for self.screen size
        """

        pygame.init()
        self.running = True

        self.screen = pygame.display.set_mode((WIDTH/2,HEIGHT/2))
        self.background = pygame.Surface((WIDTH,HEIGHT))
        self.background.fill((20,49,30))
        self.menu = pygame.surface.Surface((WIDTH/2-200,HEIGHT/2-200))
        self.menu.fill((200,255,255,0))

        self.items = {}
        for key in ITEM:
            self.items[f'{key}'] = pygame.image.load(f'src/assets/{key}.png')
        self.walls = pygame.sprite.Group()
        self.floor = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.item_group = pygame.sprite.Group()
        self.player1 = Player(TILE/2,TILE/2,\
                              (WIDTH/4,HEIGHT/4))
        self.player1.add(self.player_group)

        self.has_key = False
        self.collect_item = False
        self.door_cooldown = False
        self.action = False

        self.final_level = 2
        self.level_num = 0

        self.font = pygame.font.SysFont('Arial', 25, bold=True)

    def run(self):
        """Run method is used to start the game.
        Many pygame objects are defined in the run function.
        Calls handler functions and handles some game events
        itself.
        """


        clock = pygame.time.Clock()

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
                self.draw()
                if self.player1.clear is not True:
                    self.player_update()
                else:
                    self.action = True

            elif self.action is True and self.collect_item is True:
                self.handle_menu('item',keys)

            elif self.has_key is True and self.door_cooldown is False:
                if self.level_num == self.final_level:
                    count_to_exit -= 1/60
                    self.handle_menu('game clear',keys,count_to_exit)

                else:
                    self.handle_menu('level clear', keys)

            elif self.door_cooldown is False:
                self.handle_menu('no keys',keys)
            else:
                if keys[pygame.K_SPACE]:
                    self.player1.clear = False
                    self.action = False

            self.screen.blit(self.font.render(f'B{self.level_num}f',\
                                    True, (250, 0, 100)),(10,10))

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
        self.doors.empty()
        self.item_group.empty()

        rooms, centers = generate_rooms(20 ,WIDTH, HEIGHT, TILE)

        rp_alg = BowyerWatson(centers, WIDTH, HEIGHT)
        rp_alg.run()

        start_point, end_point, self.key_location = start_end(centers, rp_alg._all_edges)

        temporary_map = list_to_matrix(rooms,WIDTH, HEIGHT,\
                            start_point, end_point, TILE)

        mst = kruskal(rp_alg._all_edges, start_point)

        final_map = closest_walls(build_path(temporary_map,mst,TILE))

        create_objects(final_map, TILE, self.floor, self.walls, self.doors)

        self.create_items()

        self.player1.changes_x = start_point[0]-WIDTH/4
        self.player1.changes_y = start_point[1]-HEIGHT/4

        self.level_num += 1



    def player_collision(self):
        """Handler for player collisions.
        Player collisions act as triggers in the game in certain situations.
        """

        for sprite in self.walls:
            if pygame.sprite.collide_rect(self.player1, sprite):
                if self.player1.rect.bottom >= sprite.rect.top and\
                      self.player1.rect.bottom < sprite.rect.bottom:
                    self.player1.changes_y -= self.player1.velocity

                if self.player1.rect.top <= sprite.rect.bottom and\
                      self.player1.rect.top > sprite.rect.top:
                    self.player1.changes_y += self.player1.velocity

                if self.player1.rect.left <= sprite.rect.right and\
                      self.player1.rect.left > sprite.rect.left:
                    self.player1.changes_x += self.player1.velocity

                if self.player1.rect.right >= sprite.rect.left and\
                      self.player1.rect.right < sprite.rect.right:
                    self.player1.changes_x -= self.player1.velocity

        for door in self.doors:
            if pygame.sprite.collide_rect(self.player1,door)\
                and self.door_cooldown is False:
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
            self.player1.changes_x -= self.player1.velocity/1.6
            self.player1.changes_y -= self.player1.velocity/1.6
            self.player1.image = self.player1.image_left
        elif keys[pygame.K_a] and keys[pygame.K_s]:
            self.player1.changes_x -= self.player1.velocity/1.6
            self.player1.changes_y += self.player1.velocity/1.6
            self.player1.image = self.player1.image_left
        elif keys[pygame.K_d] and keys[pygame.K_w]:
            self.player1.changes_x += self.player1.velocity/1.6
            self.player1.changes_y -= self.player1.velocity/1.6
            self.player1.image = self.player1.image_right
        elif keys[pygame.K_d] and keys[pygame.K_s]:
            self.player1.changes_x += self.player1.velocity/1.6
            self.player1.changes_y += self.player1.velocity/1.6
            self.player1.image = self.player1.image_right
        elif keys[pygame.K_a]:
            self.player1.changes_x -= self.player1.velocity
            self.player1.image = self.player1.image_left
        elif keys[pygame.K_d]:
            self.player1.changes_x += self.player1.velocity
            self.player1.image = self.player1.image_right
        elif keys[pygame.K_w]:
            self.player1.changes_y -= self.player1.velocity
            self.player1.image = self.player1.image_up
        elif keys[pygame.K_s]:
            self.player1.changes_y += self.player1.velocity
            self.player1.image = self.player1.image_down




    def create_items(self):
        """Creates items from given item dictionary.
        """

        for item in self.items:
            if item == 'key':
                key = Item(TILE,\
                           (self.key_location[0]-self.key_location[0]%TILE,\
                            self.key_location[1]-self.key_location[1]%TILE),\
                           self.items[item], item)
                self.item_group.add(key)
            else:
                item_name = Item(TILE,\
                           (12*TILE,\
                            12*TILE),\
                           self.items[item], item)
                self.item_group.add(item_name)

    def draw(self):
        """Method draws the sprites contained in each group
        on to the screen.
        """
        self.screen.blit(self.background, (0,0))

        for sprite in self.walls.sprites():
            self.screen.blit(sprite.image,(sprite.x,sprite.y))
            sprite.update(self.player1)
        for sprite in self.floor.sprites():
            self.screen.blit(sprite.image,(sprite.x, sprite.y))
            sprite.update(self.player1)
        for sprite in self.doors.sprites():
            self.screen.blit(sprite.image,(sprite.x, sprite.y))
            sprite.update(self.player1)
        for item in self.item_group.sprites():
            self.screen.blit(item.image,(item.x,item.y))
            item.update(self.player1)
        for sprite in self.player_group.sprites():
            self.screen.blit(sprite.image,(sprite.x, sprite.y))




    def handle_menu(self, situation:str, keys:pygame.key.ScancodeWrapper, cd = 0):
        """Creates an ingame menu for the situation at hand.

        Args:
            situation (str): Describes the situation for the menu.
            keys (pygame.key.ScancodeWrapper): List of keys for player input.
            cd (int, optional): Countdown for exiting game. Defaults to 0.
        """
        if situation == 'item':
            item_msg = self.font.render(f'You have found a {self.collectable_item.name}',\
                                     True, (255, 0, 255))
            item_msg_rect = item_msg.get_rect()
            item_msg_rect.center = (WIDTH/4,HEIGHT/4)
            item_continue = self.font.render('Press space to collect item', True,\
                                    (255, 0, 255))
            item_continue_rect = item_continue.get_rect()
            item_continue_rect.center = (WIDTH/4,HEIGHT/4+100)
            self.screen.blit(self.menu,(100,100))
            self.screen.blit(item_continue,item_continue_rect.topleft)
            self.screen.blit(item_msg,item_msg_rect.topleft)
            if keys[pygame.K_SPACE]:
                if self.collectable_item.name == 'key':
                    self.has_key = True
                self.item_group.remove(self.collectable_item)
                self.action=False
                self.collect_item = False

        elif situation == 'no keys':
            need_key = self.font.render('The door seems to require a key...',\
                                True, (190, 0, 0))
            need_key_rect = need_key.get_rect()
            need_key_rect.center = (WIDTH/4,HEIGHT/4)
            continue_msg = self.font.render('Press space to continue',\
                                True, (190, 0, 0))
            continue_msg_rect = continue_msg.get_rect()
            continue_msg_rect.center = (WIDTH/4,HEIGHT/4+100)
            self.screen.blit(self.menu,(100,100))
            self.screen.blit(need_key,need_key_rect.topleft)
            self.screen.blit(continue_msg,continue_msg_rect.topleft)
            if keys[pygame.K_SPACE]:
                self.player1.clear = False
                self.action = False
                self.door_cooldown = True

        elif situation == 'level clear':
            level_clear = self.font.render('Press space to open door',\
                                True, (190, 0, 0))
            level_clear_rect = level_clear.get_rect()
            level_clear_rect.center = (WIDTH/4,HEIGHT/4)
            self.screen.blit(self.menu,(100,100))
            self.screen.blit(level_clear,level_clear_rect.topleft)
            if keys[pygame.K_SPACE]:
                self.has_key = False
                self.player1.clear = False
                self.action = False
                self.create_level()

        elif situation == 'game clear':
            win_msg = self.font.render('YOU WIN !', True,\
                                (255, 0, 255))
            win_msg_rect = win_msg.get_rect()
            win_msg_rect.center = (WIDTH/4,HEIGHT/4)
            cd_msg = self.font.render(f'exit in {int(cd)}',\
                                True, (255, 0, 255))
            cd_msg_rect = cd_msg.get_rect()
            cd_msg_rect.center = (WIDTH/4,HEIGHT/4+100)
            self.screen.blit(self.menu,(100,100))
            self.screen.blit(win_msg,win_msg_rect.topleft)
            self.screen.blit(cd_msg,cd_msg_rect.topleft)
            if cd <= 1:
                print("Congratulations!")
                pygame.quit()
                sys.exit()

    def possible_items(self, matrix, start, goal):
        pass
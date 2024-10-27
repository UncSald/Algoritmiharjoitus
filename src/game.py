"""Module contains the Game class.
Game class brings together multiple modules to generate a game.
The game is drawn by using the pygame library.
"""
import sys
from random import randint
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
from src.game_settings import WIDTH,HEIGHT,TILE,ITEM




class Game:
    """Class for holding data for a dungeon exploring game.
    """

    def __init__(self):
        """Class constructor for Game.
        """
        # pylint: disable=no-member
        pygame.init()
        # pylint: enable=no-member
        self.screen = pygame.display.set_mode((WIDTH/2,HEIGHT/2))
        self.background = pygame.Surface((WIDTH,HEIGHT))
        self.background.fill((20,49,30))
        self.menu = pygame.image.load('src/assets/menu.png')
        self.menu = pygame.transform.scale(self.menu,(WIDTH/2*.8,HEIGHT/2*.8))
        self.menu_rect = self.menu.get_rect()
        self.menu_rect.center = (WIDTH/4,HEIGHT/4)
        self.inventory_sprite = pygame.image.load('src/assets/inventory_slot.png')
        self.inventory_sprite = pygame.transform.scale(
            self.inventory_sprite,(
                    (self.menu.get_height()-HEIGHT*.8*.025)/4,\
                    (self.menu.get_height()-HEIGHT*.8*.025)/4
                    )
                    )
        self.font = pygame.font.SysFont('Impact', TILE)
        self.final_map :list[list]
        self.items = {}
        for key in ITEM:
            self.items[f'{key}'] = pygame.image.load(f'src/assets/{key}.png')
        self.key_location :tuple[int,int]
        self.collectable_item :Item
        self.item_locations = []
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
        self.inventory = False
        self.level_num = 0


    def run(self):
        """Run method is used to start the game.
        Many pygame objects are defined in the run function.
        Calls handler functions and handles some game events
        itself.
        """

        clock = pygame.time.Clock()
        self.create_level()
        final_level = 2
        cooldown = 5
        count_to_exit = 6

        while True:
            for event in pygame.event.get():
                # pylint: disable=no-member
                if event.type == pygame.QUIT:
                # pylint: enable=no-member
                    print("bye bye")
                    # pylint: disable=no-member
                    pygame.quit()
                    # pylint: enable=no-member
                    sys.exit()
            keys = pygame.key.get_pressed()

            if self.action is not True:
                if self.door_cooldown is True:
                    cooldown -= 1/60
                    if cooldown <= 0:
                        self.door_cooldown = False
                        cooldown = 5
                self.default_gameplay(keys)

            elif self.action and self.inventory:
                self.handle_inventory(keys)

            elif self.action is True and self.collect_item is True:
                self.handle_menu('item',keys)

            elif self.has_key and not self.door_cooldown and self.level_num == final_level:
                count_to_exit -= 1/60
                self.handle_menu('game clear',keys,count_to_exit)

            elif self.has_key and not self.door_cooldown:
                self.handle_menu('level clear', keys)

            elif self.door_cooldown is False:
                self.handle_menu('no keys',keys)
            # pylint: disable=no-member
            elif self.action and keys[pygame.K_SPACE]:
            # pylint: enable=no-member
                self.player1.clear = False
                self.action = False

            self.screen.blit(self.font.render(f'B{self.level_num}f',\
                                    True, (250, 0, 100)),(10,10))

            clock.tick(60)
            pygame.display.flip()



    def default_gameplay(self, keys:pygame.key.ScancodeWrapper):
        """Generates the default gameplay experience.
        Gameplay without menus.

        Args:
            keys (pygame.key.ScancodeWrapper): Keys pressed.
        """
        # pylint: disable=no-member
        if keys[pygame.K_i]:
        # pylint: enable=no-member
            self.menu = pygame.transform.scale(self.menu,\
                                               (HEIGHT/2*.8,HEIGHT/2*.8))
            self.menu_rect = self.menu.get_rect()
            self.menu_rect.center = (WIDTH/4,HEIGHT/4)
            self.inventory = True
            self.action = True
        self.draw()
        if self.player1.clear is not True:
            self.player_update()
        else:
            self.action = True



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

        start_point, end_point, self.key_location = start_end(centers,\
                                                              rp_alg.all_edges)

        temporary_map = list_to_matrix(rooms,WIDTH, HEIGHT,\
                            start_point, end_point, TILE)

        mst = kruskal(rp_alg.all_edges, start_point)

        self.final_map = closest_walls(build_path(temporary_map,mst,TILE))

        create_objects(self.final_map, TILE, self.floor, self.walls, self.doors)

        self.possible_items()

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

        self.player1.record_changes(0,0)
        self.player_collision()
        keys = pygame.key.get_pressed()
        # pylint: disable=no-member
        if keys[pygame.K_a] and keys[pygame.K_w]:
        # pylint: enable=no-member
            self.player1.record_changes(-self.player1.velocity/1.6,-self.player1.velocity/1.6)
            self.player1.image = self.player1.image_left
        # pylint: disable=no-member
        elif keys[pygame.K_a] and keys[pygame.K_s]:
        # pylint: enable=no-member
            self.player1.record_changes(-self.player1.velocity/1.6,self.player1.velocity/1.6)
            self.player1.image = self.player1.image_left
        # pylint: disable=no-member
        elif keys[pygame.K_d] and keys[pygame.K_w]:
        # pylint: enable=no-member
            self.player1.record_changes(self.player1.velocity/1.6,-self.player1.velocity/1.6)
            self.player1.image = self.player1.image_right
        # pylint: disable=no-member
        elif keys[pygame.K_d] and keys[pygame.K_s]:
        # pylint: enable=no-member
            self.player1.record_changes(self.player1.velocity/1.6,self.player1.velocity/1.6)
            self.player1.image = self.player1.image_right
        # pylint: disable=no-member
        elif keys[pygame.K_a]:
        # pylint: enable=no-member
            self.player1.record_changes(-self.player1.velocity,0)
            self.player1.image = self.player1.image_left
        # pylint: disable=no-member
        elif keys[pygame.K_d]:
        # pylint: enable=no-member
            self.player1.record_changes(self.player1.velocity,0)
            self.player1.image = self.player1.image_right
        # pylint: disable=no-member
        elif keys[pygame.K_w]:
        # pylint: enable=no-member
            self.player1.record_changes(0,-self.player1.velocity)
            self.player1.image = self.player1.image_up
        # pylint: disable=no-member
        elif keys[pygame.K_s]:
        # pylint: enable=no-member
            self.player1.record_changes(0,self.player1.velocity)
            self.player1.image = self.player1.image_down




    def create_items(self):
        """Creates items from given item dictionary.
        """
        players_items = []
        for players_item in self.player1.items:
            players_items.append(players_item.name)
        for index, item in enumerate(self.items):
            if item == 'key':
                key = Item(TILE,\
                           (self.key_location[0]-self.key_location[0]%TILE,\
                            self.key_location[1]-self.key_location[1]%TILE),\
                           self.items[item], item)
                self.item_group.add(key)
            else:
                if item not in players_items:
                    new_item = Item(TILE,\
                            self.item_locations[index],\
                            self.items[item], item)
                    self.item_group.add(new_item)


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
            message = self.font.render(f'You have found a {self.collectable_item.name}',\
                                     True, (0, 0, 0))
            message_rect = message.get_rect()
            message_rect.center = (WIDTH/4,HEIGHT/4)
            message2 = self.font.render('Press space to collect item', True,\
                                    (0, 0, 0))
            message2_rect = message2.get_rect()
            message2_rect.center = (WIDTH/4,HEIGHT/4+100)
            # pylint: disable=no-member
            if keys[pygame.K_SPACE]:
            # pylint: enable=no-member
                if self.collectable_item.name == 'key':
                    self.has_key = True
                self.item_group.remove(self.collectable_item)
                self.player1.add_item(self.collectable_item)
                self.action=False
                self.collect_item = False

        elif situation == 'no keys':
            message = self.font.render('The door seems to require a key...',\
                                True, (0, 0, 0))
            message_rect = message.get_rect()
            message_rect.center = (WIDTH/4,HEIGHT/4)
            message2 = self.font.render('Press space to continue',\
                                True, (0, 0, 0))
            message2_rect = message2.get_rect()
            message2_rect.center = (WIDTH/4,HEIGHT/4+100)
            # pylint: disable=no-member
            if keys[pygame.K_SPACE]:
            # pylint: enable=no-member
                self.player1.clear = False
                self.action = False
                self.door_cooldown = True

        elif situation == 'level clear':
            message = self.font.render('Press space to open door',\
                                True, (0, 0, 0))
            message_rect = message.get_rect()
            message_rect.center = (WIDTH/4,HEIGHT/4)
            message2 = self.font.render('',\
                                True, (0, 0, 0))
            message2_rect = message2.get_rect()
            message2_rect.center = (WIDTH/4,HEIGHT/4+30)
            # pylint: disable=no-member
            if keys[pygame.K_SPACE]:
            # pylint: enable=no-member
                for item in self.player1.items:
                    if item.name == 'key':
                        self.player1.remove_item(item)
                self.has_key = False
                self.player1.clear = False
                self.action = False
                self.create_level()

        elif situation == 'game clear':
            message = self.font.render('YOU WIN !', True,\
                                (0, 0, 0))
            message_rect = message.get_rect()
            message_rect.center = (WIDTH/4,HEIGHT/4)
            message2 = self.font.render(f'exit in {int(cd)}',\
                                True, (0, 0, 0))
            message2_rect = message2.get_rect()
            message2_rect.center = (WIDTH/4,HEIGHT/4+100)
            self.screen.blit(self.menu,self.menu_rect)
            self.screen.blit(message,message_rect.topleft)
            self.screen.blit(message2,message2_rect.topleft)
            if cd <= 1:
                print("Congratulations!")
                # pylint: disable=no-member
                pygame.quit()
                # pylint: enable=no-member
                sys.exit()
        self.screen.blit(self.menu,self.menu_rect)
        self.screen.blit(message,message_rect.topleft)
        self.screen.blit(message2,message2_rect.topleft)

    def possible_items(self):
        """Selects possible locations for items on the map.
        """
        self.item_locations.clear()
        possible_locations = []
        for y, col in enumerate(self.final_map):
            for x, value in enumerate(col):
                if value == 1 and (x*TILE,y*TILE) != self.key_location:
                    possible_locations.append((x*TILE,y*TILE))
        for _ in enumerate(self.items):
            slot = randint(3,10)
            pick = randint(1,slice-1)
            area_end = (len(possible_locations))//slot
            area_start = area_end*pick
            index = randint(area_start,len(possible_locations)-1)
            item_location = possible_locations[index]
            possible_locations.remove(item_location)
            self.item_locations.append(item_location)



    def handle_inventory(self, keys:pygame.key.ScancodeWrapper):
        """Handles drawing correct inventory on the screen.

        Args:
            keys (pygame.key.ScancodeWrapper): List of keys pressed in wrapper.
        """
        menu_font = pygame.font.SysFont('Impact', TILE//2.5)
        # pylint: disable=no-member
        if keys[pygame.K_ESCAPE]:
        # pylint: enable=no-member
            self.inventory = False
            self.action = False
            self.menu = pygame.transform.scale(self.menu,(WIDTH/2*.8,HEIGHT/2*.8))
            self.menu_rect = self.menu.get_rect()
            self.menu_rect.center = (WIDTH/4,HEIGHT/4)
        offset = HEIGHT/2*.8*.025
        self.screen.blit(self.menu,self.menu_rect)
        y_mod = 0
        for i in range(16):
            if i%4 == 0:
                y_mod = i/4
            x_pos = offset+i%4*self.inventory_sprite.get_height()\
                +(WIDTH/4-self.menu.get_width()/2)
            y_pos = offset+y_mod*self.inventory_sprite.get_height()\
                +(HEIGHT/4-self.menu.get_height()/2)
            self.screen.blit(self.inventory_sprite,(x_pos,y_pos))
            if i < self.player1.item_count():
                item = self.player1.get_item(i)
                item_image = pygame.transform.scale(item.image,\
                                                        (HEIGHT/8*.8,HEIGHT/8*.8))
                item_rect = item_image.get_rect()
                item_rect.center = (x_pos+self.inventory_sprite.get_height()/2,\
                                    y_pos+self.inventory_sprite.get_height()/2)
                self.screen.blit(item_image,(x_pos,y_pos))
                item_name = menu_font.render(f'{item}', True,\
                                    (0, 0, 0))
                item_name_rect = item_name.get_rect()
                item_name_rect.center = (x_pos+self.inventory_sprite.get_height()/2\
                                         ,y_pos+self.inventory_sprite.get_height()*.8)
                self.screen.blit(item_name,item_name_rect)

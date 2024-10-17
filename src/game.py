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
        self.running = True
        self.widht = widht
        self.height = height
        self.tile_size = tile
        self.final_level = 1
        self.level_num = 0

    def run(self):


        # INIT PYGAME
        pygame.init()


        # ADD BACKGROUND COLOR, FEEL FREE TO CHANGE IT
        BG = pygame.Surface((self.widht,self.height))
        BG.fill('black')
        # DEFINE SCREEN SIZE AND self.height
        # SCREEN SIZE CAN BE CHANGED BUT SHOULD YOU CHANGE IT
        # REMEMBER TO CHANGE THE PLAYER POSITION, AND
        # CHANGES_X/Y ACCORDINGLY
        screen = pygame.display.set_mode((self.widht/2,self.height/2))
        
        # CREATE LEVEL
        self.level = self.create_level()
        self.level_num += 1
        
        # DEFINE CLOCK FOR SMOOTH SAILING
        clock = pygame.time.Clock()

        # MAIN LOOP
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # DRAW ALL SPRITES IN GROUPS
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
            self.player1.update()
            if self.player1.clear:
                self.level = self.create_level()
                self.level_num += 1

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
        temporaty_map = list_to_matrix(rooms,centers,self.widht, self.height,\
                            start_point, self.end_point, self.tile_size)
        print(f"map done, {len(temporaty_map[0])}x{len(temporaty_map)} tiles")

        # CREATE MINIMUM SPANNING TREE FROM EDGES IN TRIANGULATION
        mst = kruskal(rp_alg._all_edges, start_point)
        print(f"kruskal done")

        # CREATE FINAL MAP FROM TEMPORARY ONE
        # THIS TIME IT CONTAINS PATHS BETWEEN ROOMS CREATED
        # BY A_STAR
        MAP = build_path(temporaty_map,mst,self.tile_size)
        print(f"final map done")

        create_objects(MAP, self.tile_size, self.floor, self.walls, self.doors)
        print(f"create objects done")

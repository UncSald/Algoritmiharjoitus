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


# DEFINE MAIN FUNCTION
def main():

    # DEFINE WIDTH, HEIGHT, AND TILE SIZE.
    # FEEL FREE TO CHANGE THESE AND SEE HOW THE MAP GENERATES
    WIDTH = 1500
    HEIGHT = 1000
    tile_size = 32

    # GENERATE ROOMS AND TAKE THEIR COORDINATES AND CENTER POINTS
    rooms_gened = generate_rooms(25 ,WIDTH, HEIGHT, tile_size)
    rooms, centers = rooms_gened
    print(f"rooms done")

    # INIT AND RUN BOWYER-WATSON -ALGORITHM
    # AS INPUT GIVE IT THE ROOM CENTERS, AND SCREEN SIZE
    rp_alg = BowyerWatson(centers, WIDTH, HEIGHT)
    rp_alg.run()
    print(f"rp_alg done")

    # DEFINE STARTPOINT AND ENDPOINT
    start_point, end_point = start_end(centers)

    # CREATE MAP CONTAINING ROOMS, START, AND GOAL
    temporaty_map = list_to_matrix(rooms,centers,WIDTH, HEIGHT,\
                         start_point, end_point, tile_size)
    print(f"map done, {len(temporaty_map[0])}x{len(temporaty_map)} tiles")
    # CREATE MINIMUM SPANNING TREE FROM EDGES IN TRIANGULATION
    mst = kruskal(rp_alg._all_edges, start_point)
    print(f"kruskal done")
    # CREATE FINAL MAP FROM TEMPORARY ONE
    # THIS TIME IT CONTAINS PATHS BETWEEN ROOMS CREATED
    # BY A_STAR
    MAP = build_path(temporaty_map,mst,tile_size)
    print(f"final map done")
    # DEFINE GROUPS FOR WALLS, FLOOR, AND PLAYER
    walls = pygame.sprite.Group()
    floor = pygame.sprite.Group()
    player = pygame.sprite.Group()
    create_objects(MAP, floor, walls, tile_size)
    print(f"create objects done")
    # DEFINE PLAYER AND START POINT FOR CORRECT MAP POSITION
    player1 = Player(tile_size/2,tile_size/2,(WIDTH/4,HEIGHT/4), walls)
    player1.add(player)
    player1.changes_x = start_point[0]-WIDTH/4
    player1.changes_y = start_point[1]-HEIGHT/4

    # INIT PYGAME
    pygame.init()

    # ADD BACKGROUND COLOR, FEEL FREE TO CHANGE IT
    BG = pygame.Surface((WIDTH,HEIGHT))
    BG.fill('black')
    # DEFINE SCREEN SIZE AND HEIGHT
    # SCREEN SIZE CAN BE CHANGED BUT SHOULD YOU CHANGE IT
    # REMEMBER TO CHANGE THE PLAYER POSITION, AND
    # CHANGES_X/Y ACCORDINGLY
    screen = pygame.display.set_mode((WIDTH/2,HEIGHT/2))

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
        for sprite in walls:
            screen.blit(sprite.image,(sprite.x,sprite.y))
            sprite.update(player1)
        for sprite in floor:
            screen.blit(sprite.image,(sprite.x, sprite.y))
            sprite.update(player1)
        for sprite in player:
            screen.blit(sprite.image,(sprite.x, sprite.y))   

        # UPDATE PLAYER
        player1.update()

        clock.tick(60)
        pygame.display.flip()




if __name__ == "__main__":
    main()

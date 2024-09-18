import sys
import pygame
import pygame.gfxdraw
from bowyerWatson import BowyerWatson
from roomGeneration import generate_rooms, start_end
from listMatrix import list_to_matrix
from kruskal import kruskal
from a_star import build_path




def main():
    WIDTH = 1500
    HEIGHT = 1000
    screen = pygame.display.set_mode((WIDTH,HEIGHT))



    rooms_gened = generate_rooms(20,WIDTH, HEIGHT)
    rooms = rooms_gened[0]
    centers = rooms_gened[1]


    rp_alg = BowyerWatson(centers, WIDTH, HEIGHT)
    rp_alg.run()


    start_point, end_point = start_end(centers)

    MAP = list_to_matrix(rooms,centers,WIDTH, HEIGHT, start_point, end_point)

    mst = kruskal(rp_alg._all_edges, start_point)

    final_map = build_path(MAP,mst)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        y=0
        for row in final_map:
            x=0
            for column in row:
                if column == 1:
                    pygame.draw.rect(screen,'blue',[x*32,y*32,32,32])
                elif column == 5:
                    pygame.draw.rect(screen,'red',[x*32,y*32,32,32])
                elif column == 2:
                    pygame.draw.rect(screen,'green',[x*32,y*32,32,32])
                elif column == 3 or column == 4:
                    pygame.draw.rect(screen,'black',[x*32,y*32,32,32])
                else:
                    pygame.draw.rect(screen,'white',[x*32,y*32,32,32])
                x+=1
            y+=1
        pygame.display.update()


if __name__ == "__main__":
    main()

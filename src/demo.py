import sys
import pygame
import pygame.gfxdraw
from src.bowyerWatson import BowyerWatson
from src.roomGeneration import generate_rooms, start_end

def demo():
    pygame.init()
    WIDTH = 1500
    HEIGHT = 900
    TILESIZE = 1


    rooms1, centers1 = generate_rooms(20,WIDTH,HEIGHT,32)
    bowyer_watson1 = BowyerWatson(centers1,WIDTH,HEIGHT)
    bowyer_watson1.run()

    rooms2, centers2 = generate_rooms(200,WIDTH,HEIGHT,TILESIZE)
    bowyer_watson2 = BowyerWatson(centers2,WIDTH,HEIGHT)
    bowyer_watson2.run()

    rooms3, centers3 = generate_rooms(2000,WIDTH,HEIGHT,TILESIZE)
    bowyer_watson3 = BowyerWatson(centers3,WIDTH,HEIGHT)
    bowyer_watson3.run()


    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    background = pygame.surface.Surface((WIDTH,HEIGHT))
    background.fill('black')
    clock = pygame.time.Clock()
    timer = 0
    countdown1 = 5
    countdown2 = 5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("bye bye")
                pygame.quit()
                sys.exit()
        screen.blit(background,(0,0))
        if timer < 15:
            for room in rooms1:
                room.draw(screen,'blue')
            
            if countdown1 <= 0:
                for triangle in bowyer_watson1._triangulation:
                    if countdown2 <= 0:
                        triangle.draw(screen,'red', 1)
                    else:
                        triangle.draw(screen,'red',0)
                countdown2-=1/60
            countdown1 -= 1/60
        
        elif timer < 30:
            if countdown1 <= -5 and timer < 20:
                countdown1 = 5
            for room in rooms2:
                room.draw(screen,'blue')
            
            if countdown1 <= 0:
                for triangle in bowyer_watson2._triangulation:
                        triangle.draw(screen,'red',0)
            countdown1 -= 1/60

        else:
            if countdown1 <= -5 and timer < 35:
                countdown1 = 5
            for room in rooms3:
                room.draw(screen,'blue')
            if countdown1 <= 0:
                for triangle in bowyer_watson3._triangulation:
                        triangle.draw(screen,'red',0)
            countdown1 -= 1/60
        


        timer += 1/60

        clock.tick(60)
        pygame.display.flip()
        
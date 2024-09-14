import sys
import pygame
import pygame.gfxdraw
from geometry import Triangle

if __name__ == "__main__":
    pygame.init()

    WIDTH = 1500
    HEIGHT = 1000
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((0,0,0))
    color = 'red'

    triangle = Triangle(((100,100),(100,200)),((100,100),(150,150)),((100,200),(150,150)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        triangle.draw(screen, color)

        pygame.display.update()

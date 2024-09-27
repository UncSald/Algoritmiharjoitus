import sys
import pygame
import pygame.gfxdraw
from random import randint
from bowyerWatson import BowyerWatson
from roomGeneration import generate_rooms
from listMatrix import list_to_matrix
from kruskal import kruskal
from a_star import build_path

# TESTER FOR GENERATE_ROOMS FUNCTION
def test_generate_rooms():
    pass

# TESTER FOR BOWYER-WATSON ALGORITHM
def test_bowyer_watson(amount):
    width1 = 1499
    height1 = 999
    points = set()
    over_double = False
    for i in range(amount):
        point = (randint(0,width1),randint(0,height1))
        points.add(point)
    algortithm1 = BowyerWatson(points,width1,height1)
    algortithm1.run()
    if len(algortithm1._triangulation) > (2*amount)+(amount/10):
        over_double = True
        pygame.init()
        clock = pygame.time.Clock()
        surface = pygame.display.set_mode((width1,height1))
        surface.fill('black')
        tick = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            tick += 1
            for triangle in algortithm1._triangulation:
                triangle.draw(surface,'red')
            pygame.display.flip()
            clock.tick(3)
    print(f"points on list: {len(points)}")
    print(f"triangles drawn: {len(algortithm1._triangulation)}")

    return over_double

# TESTER FOR LIST_TO_MATRIX FUNCTION
def list_to_matrix():
    pass

# TESTER FOR A_STAR
def test_a_star():
    pass

# TESTER FOR BUILD_PATH
def test_build_path():
    pass

if __name__ == "__main__":
    count = 0
    amount = 60
    for i in range(1000):
        print(i)
        if test_bowyer_watson(amount):
            count += 1
    print(f"failure rate : {count/50*100}%")

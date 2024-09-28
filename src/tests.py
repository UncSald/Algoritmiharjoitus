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
        point = (randint(0,width1-1),randint(0,height1-1))
        points.add(point)
    algortithm1 = BowyerWatson(points,width1,height1)
    algortithm1.run()
    if len(algortithm1._triangulation) > (2*amount)+(amount/10):
        over_double = True

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
    print("Tester for Bowyer-Watson -algorithm, this may take a couple of minutes.")
    for i in range(10):
        count = 0
        amount = [10,30,50,80,100,200,400,500,700,1000]
        times = 1000
        if amount[i] >= 400:
            times = 100
        for j in range(times):
            if test_bowyer_watson(amount[i]):
                count += 1
        print(f"Failure rate with {amount[i]} points, and {times} runs: {count/times*100}%")

from random import randint
from src.geometry import Rectangle

# FUNCTION WHICH GENERATES RECTANGLES WHEN GIVEN
# THE MAX AMOUNT OF RECTANGLES CREATED AND THE SIZE
# OF THE SIZE OF THE AREA WHERE RECTANGLES WILL BE DRAWN
# ON. RETURNS A SET OF RECTANGLES AND A SET OF THEIR 
# CENTER POINTS.

def generate_rooms(count :int, width :int, height :int, tile_size :int):
    rect_set = set()
    point_set = set()


    if count < 10:
        if (49*count)/((width/tile_size)*(height/tile_size)) > 0.70:
            raise ValueError("tilesize too high for this width and height.")
    elif (49*count*0.25)/((width/tile_size)*(height/tile_size)) > 0.20:
        raise ValueError("tilesize too high for this width and height.")

    while len(rect_set) < count:
        x_point = randint(1, ((width-(width%tile_size))//tile_size))*tile_size
        y_point = randint(1, ((height-(height%tile_size))//tile_size))*tile_size
        max_width = int((width-x_point)//tile_size)-1
        max_height = int((height-y_point)//tile_size)-1
        if max_width < 4 or max_height < 4:
            continue
        if max_width > 7:
            max_width = 7
        if max_height > 7:
            max_height = 7
        rect_width = int(randint(3, max_width)*tile_size)
        rect_height = int(randint(3, max_height)*tile_size)
        new_rect = Rectangle((x_point,y_point), rect_width, rect_height)
        collision = False
        for rect in rect_set:
            if rect.collision(new_rect):
                collision = True
        if not collision:
            rect_set.add(new_rect)
            point_set.add(new_rect.center)
    return (rect_set, point_set)



# FUNCTION TO DEFINE A START POINT AND END POINT IN THE MAP
def start_end(points :set, edges):
    temp_points = points.copy()
    start = temp_points.pop()
    for edge in edges:
        end = edge[0]
        if (start,end) not in edges and (end,start) not in edges and start!=end:
            for scnd_edge in edges:
                key = scnd_edge[0]
                if (start,key) not in edges and (key,start) not in edges and\
                      (key,end) not in edges and (end,key) not in edges and key!=end and key!=start:
                    return start, end, key

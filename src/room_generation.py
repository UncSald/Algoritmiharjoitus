"""Contains generate_rooms function, and start_end function.
These functions are used to generate objects to random locations
on a given plane.

    Raises:
        ValueError: Raises error if the tile size, room count,
        and given area don't match. In cases where room count is less, the
        area reserved for new rectangles must be larger.
        ValueError: Raises error if the tile size, room count,
        and given area don't match. When room count is high enough, the average
        room size goes down, and we can leave less space for new rooms.

    Returns:
        tuple[set,set]: A set containing rectangle objects, and a set containing 
        the rectangles' center points.
"""

from random import randint
from src.geometry import Rectangle

def generate_rooms(count :int, width :int, height :int, tile_size :int):
    """Generates a set of Rectangle class objects whih do not overlap
    on the given plane.

    Args:
        count (int): Number of rooms to be generated.
        width (int): Width of the draw area.
        height (int): Height of the draw area.
        tile_size (int): Size of a single tile in the matrix where rooms will be inserted.

    Raises:
        ValueError: Error in the situation a tile size, area size,
        and count don't match. Mismatch can create an eternal loop.
        ValueError: Error in the situation a tile size, area size,
        and count don't match. Mismatch can create an eternal loop.

    Returns:
        tuple[set,set]: Two sets, the first contains rectangles,
        and the second contains the center points of each rectangle.
    """
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
        max_width = min(max_width,7)
        max_height = min(max_height,7)
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
def start_end(points :set, edges:set):
    """Define three random points from a list of edges.
    These points cannot have a direct connection with eachother.

    Args:
        points (set): A set of points.
        edges (set): A set of edges created from these points.

    Returns:
        tuple[int,int,int]: Three different points.
    """
    temp_points = points.copy()
    start = temp_points.pop()
    for edge in edges:
        end = edge[0]
        if (start,end) not in edges and (end,start) not in edges and start!=end:
            for scnd_edge in edges:
                key = scnd_edge[0]
                if (start,key) not in edges and (key,start) not in edges and\
                      (key,end) not in edges and (end,key) not in edges and key not in (start,end):
                    return start, end, key
    return None

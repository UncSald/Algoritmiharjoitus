from src.geometry import Rectangle

# LIST TO MATRIX TAKES A LIST OF RECTANGLES AND A LIST OF THEIR CENTERS
# AS PARAMETERS
# IT THEN RETURNS THE ROOMS AND THEIR CENTERS PLACED IN A MATRIX


def list_to_matrix(rooms :list, room_centers :list, width :int,\
                   height :int, start :tuple[int,int], end:tuple[int,int], tile_size :int):
    matrix = []
    for i in range((height-height%tile_size)//tile_size):
        matrix.append([])
    for row in matrix:
        for i in range((width-width%tile_size)//tile_size):
            row.append(0)
    for room in rooms:
        for point in rect_to_coord(room, tile_size):
            x,y = point
            matrix[y][x] = 1
    for point in room_centers:
        x, y = point_to_coord(point, tile_size)
        if point == start:
            matrix[y][x] = 3
        elif point == end:
            matrix[y][x] = 4
        else:
            matrix[y][x] = 1
    y = 0
    for row in matrix:
        x = 0
        for column in row:
            if y == 0 or x == 0 or x == len(row)-1 or y == len(matrix)-1:
                matrix[y][x] = 9
            x+=1
        y+=1
    return matrix

# GIVES OUT COORDINATES FOR A POINT IN A MATRIX
# WITH SET TILESIZE
def point_to_coord(point: tuple[int,int], tile_size:int):
    x = int((point[0]-point[0]%tile_size)//tile_size)
    y = int((point[1]-point[1]%tile_size)//tile_size)
    return (x,y)

# GIVES OUT COORDINATES FOR A RECTANGLE IN A MATRIX
# WITH SET TILESIZE

def rect_to_coord(rect :Rectangle, tile_size :int):
    coords = []
    x, y = rect.edges[0][0]
    x = int(x//tile_size)
    y = int(y//tile_size)
    width = rect.width//tile_size
    height = rect.height//tile_size
    for r in range(height):
        for c in range(width):
            coords.append((x+c,y+r))
    return coords

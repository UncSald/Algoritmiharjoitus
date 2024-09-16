# LIST TO MATRIX TAKES A LIST OF RECTANGLES AND A LIST OF THEIR CENTERS
# AS PARAMETERS
# IT THEN RETURNS THE ROOMS AND THEIR CENTERS PLACED IN A MATRIX


def list_to_matrix(rooms :list, room_centers :list, width, height):
    matrix = []
    for i in range((height-height%32)//32):
        matrix.append([])
    for row in matrix:
        for i in range((width-width%32)//32):
            row.append(0)
    for room in rooms:
        for point in rect_to_coord(room):
            x,y = point
            matrix[y][x] = 2
    for point in room_centers:
        x, y = point_to_coord(point)
        matrix[y][x] = 1
        print(x,y)
    return matrix

def point_to_coord(point):
    x = int((point[0]-point[0]%32)//32)
    y = int((point[1]-point[1]%32)//32)
    return (x,y)

def rect_to_coord(rect):
    coords = []
    print(rect.edges[0][0])
    x, y = rect.edges[0][0]
    x = int(x//32)
    y = int(y//32)
    width = rect.width//32
    height = rect.height//32
    for r in range(height):
        for c in range(width):
            coords.append((x+c,y+r))
    return coords

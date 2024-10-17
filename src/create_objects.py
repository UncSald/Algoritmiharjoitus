from src.sprites import Floor, Wall, Door



# FUNCTION CREATES OBJECTS AND ADDS THEM TO CORRECT GROUPS
# SO THEY WILL BE DRAWN CORRECTLY
def create_objects(matrix :list, floor, walls, tile_size :int):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):

            if matrix[row][column] == 1:
                new_tile = Floor(tile_size, tile_size,\
                                 (column*tile_size, row*tile_size),1)
                new_tile.add(floor)
            elif matrix[row][column] == 2:
                new_tile = Floor(tile_size, tile_size,\
                                 (column*tile_size, row*tile_size),2)
                new_tile.add(floor)
            elif matrix[row][column] == 3:
                new_tile = Door(tile_size, tile_size,\
                                 (column*tile_size, row*tile_size),3)
                new_tile.add(floor)
            elif matrix[row][column] == 4:
                new_tile = Door(tile_size, tile_size,\
                                 (column*tile_size, row*tile_size),4)
                new_tile.add(floor)
            else:
                new_tile = Wall(tile_size, tile_size,\
                                (column*tile_size, row*tile_size))
                new_tile.add(walls)
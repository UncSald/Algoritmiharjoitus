from sprites import Floor, Wall, Door




def create_objects(matrix, floor, walls, tile_size):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):

            if matrix[row][column] == 1:
                new_tile = Floor(tile_size, tile_size,\
                                 (column*tile_size, row*tile_size))
                new_tile.add(floor)
            elif matrix[row][column] == 2:
                new_tile = Floor(tile_size, tile_size,\
                                 (column*tile_size, row*tile_size))
                new_tile.add(floor)
            elif matrix[row][column] == 3:
                new_tile = Door(tile_size, tile_size,\
                                 (column*tile_size, row*tile_size))
                new_tile.add(floor)
            elif matrix[row][column] == 4:
                new_tile = Door(tile_size, tile_size,\
                                 (column*tile_size, row*tile_size))
                new_tile.add(floor)
            else:
                new_tile = Wall(tile_size, tile_size,\
                                (column*tile_size, row*tile_size))
                new_tile.add(walls)
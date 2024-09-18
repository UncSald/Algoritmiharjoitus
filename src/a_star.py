import queue




def a_star(matrix, start_point, end_point):
    passed = queue.PriorityQueue(0)
    passed.put((start_point, 0))
    came_from = {}
    cost_so_far = {}
    came_from[start_point] = None
    cost_so_far[start_point] = 0

    while not passed.empty():
        location = passed.get()[0]

        if location == end_point:
            break

        for next in matrix[location]:
            cost = cost_so_far[location] + 1
            if next[0] not in cost_so_far or cost < cost_so_far[next[0]]:
                cost_so_far[next[0]] = cost
                priority = cost + heuristics(next[0], end_point)
                passed.put((next[0], priority))
                came_from[next[0]] = location
    
    return came_from, cost_so_far





def heuristics(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1-x2) + abs(y1-y2)





def weighted_graph(matrix):
    nodes = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            a = (row,column)
            nodes.append(a)
    map = {node : [] for node in nodes}
    for node in nodes:
        if node == (0,0):
            new_edge(node, (0,1), map)
            new_edge(node, (1,0), map)
        elif node == (len(matrix)-1,len(matrix[0])-1):

            new_edge(node, (len(matrix)-2,len(matrix[0])-1),map)
            new_edge(node, (len(matrix)-1,len(matrix[0])-2),map)
        elif node == (0,len(matrix[0])-1):
            new_edge(node,(0,len(matrix[0])-2),map)
            new_edge(node,(1,node[1]),map)
        elif node[0] == 0:
            new_edge(node,(0,node[1]-1),map)
            new_edge(node,(1,node[1]),map)
            new_edge(node, (0,node[1]+1),map)

        elif node[1] == 0:
            new_edge(node,(node[0]-1,0),map)
            new_edge(node,(node[0],1),map)
            new_edge(node, (node[0]+1,0),map)
        elif node[0] == len(matrix)-1:
            new_edge(node,(len(matrix)-1,node[1]-1),map)
            new_edge(node,(len(matrix)-2,node[1]),map)
            new_edge(node, (len(matrix)-1,node[1]+1),map)
        elif node[1] == len(matrix[0])-1:
            new_edge(node,(node[0]-1,len(matrix[0])-1),map)
            new_edge(node,(node[0],len(matrix[0])-2),map)
            new_edge(node, (node[0]+1,len(matrix[0])-1),map)
        else:
            new_edge(node,(node[0],node[1]-1),map)
            new_edge(node,(node[0],node[1]+1),map)  
            new_edge(node,(node[0]-1,node[1]),map)
            new_edge(node,(node[0]+1,node[1]),map)
    return map




def new_edge(node_a, node_b, map):
    map[node_a].append((node_b, 1))

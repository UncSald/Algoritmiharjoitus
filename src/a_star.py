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

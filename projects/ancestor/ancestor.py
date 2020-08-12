from graph import Graph
from queue import Queue
from util import Stack

def earliest_ancestor(ancestors, start):
    graph = Graph()
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)

    q = Queue()
    q.enqueue([start])
    longest_path = 1
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()
        current_node = path[-1]

        if len(path) >= longest_path and current_node < earliest_ancestor:
            if current_node < earliest_ancestor:
                earliest_ancestor = current_node
        if len(path) > longest_path:
            longest_path = len(path)
            earliest_ancestor = current_node
        

        neighbors = graph.get_neighbors(current_node)
        print(neighbors)
        for ancestor in neighbors:
            path_copy = path[:]
            path_copy.append(ancestor)
            q.enqueue(path_copy)

    return earliest_ancestor


    

    # print(f'Graph: {ancestors_list}')
earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 9)
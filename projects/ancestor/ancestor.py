from graph import Graph
from queue import Queue
from util import Stack

def earliest_ancestor(ancestors, start):
    graph = Graph()                         # init graph
    for parent, child in ancestors:         # populate it with vertices (ancestors) and add edges (connections)
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)

    q = Queue()                             # start our queue
    q.enqueue([start])                      # enqueue a path with the starting vertex
    longest_path = 1                        # longest path defaults to 1 because we are always given a vertex to start from
    earliest_ancestor = -1

    while q.size() > 0:                     # while our queue size is greater than 0...
        path = q.dequeue()                  # assign whatever we dequeue to our path variable
        current_node = path[-1]             #current_node will be whatever is at the end of our path array
        """
        first IF:
            if the length of our path is greater than or equal to what longest_path currently is
            AND our current_node is less than what our earliest_ancestor currentyl is, then
            earliest_ancestor will be whatever our current_node is
        
        second IF:
            if the length of our path is greater than whatever our longest_path currently is, then
            longest_path will be the length of path and earliest_ancestor will be current_node
        """
        if len(path) >= longest_path and current_node < earliest_ancestor:  
                earliest_ancestor = current_node
        if len(path) > longest_path:
            longest_path = len(path)
            earliest_ancestor = current_node
        
        neighbors = graph.get_neighbors(current_node)   # get the neighbors from the current node
        # print(neighbors)
        for ancestor in neighbors:                      # for each ancestor we get from neighbors
            # print(f'ancestor: {ancestor}')
            path_copy = path[:]                         # create a path_copy and append that ancestor to path_copy
            path_copy.append(ancestor)    
            print(f'COPY: {path_copy}')              
            q.enqueue(path_copy)                        # enqueue path_copy similar to how we did with our start
            print(f'SIZE: {q.size()}')
        
        """
        our loop will end whenever we enqueue something with
        the length of 0, otherwise this for loop is basically
        the engine to our while loop
        """
    if q.size() <= 0:
        print('size has reached zero')

    # return whatever our earliest_ancestor ends up being
    return earliest_ancestor


    

    # print(f'Graph: {ancestors_list}')
earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 9)
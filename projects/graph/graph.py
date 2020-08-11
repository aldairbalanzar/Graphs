"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    #---- VERTICES CONTAINTER (dictionary) ----#
    def __init__(self):                                         # initiate somewhere to store vertices
        self.vertices = {}

    #---- ADD VERTEX ----#
    def add_vertex(self, vertex_id):                            # in the vertices dictionary, add that vertex to the set
        self.vertices[vertex_id] = set()

    #---- ADD EDGE ----#
    def add_edge(self, v1, v2):                                 # in the vertices dictionary, if vertex 1 (vertex_id) is in the dictionary, add the second vertex to vertex 1's set
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist.')
    
    #---- GET NEIGHBORS ----#
    def get_neighbors(self, vertex_id):                         # Get the neighbors (connections, values in that vertex' set)
        return self.vertices[vertex_id]


    ########## Traversal ##########


    def bft(self, starting_vertex):     # traverse through graph in a breadth-first manner
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()                                 # init queue
        q.enqueue(starting_vertex)                  # add starting vertex to queueu
        visited = set()                             # while the size of the queue is greater than 0...
        while q.size() > 0:                         # assign the current vertex to a variable
            current = q.dequeue()                   # current is whatever is dequeued from our queue
            if current not in visited:                  # if current is not in visited...
                visited.add(current)                    # add it to visited
                print(f'{current}')                     
                neighbors = self.get_neighbors(current) # get the neighbors of current vertex (current)
                for neighbor in neighbors:              # for every neighbor...
                    q.enqueue(neighbor)                 # add it to the queue (keeps the loop going until we can't enqueue anymore and our que size is 0)

    def dft(self, starting_vertex):    # traverse through graph in a depth-first manner
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()                    # init stack
        visited = set()                    # init a visited set (a set so we don't get duplicates)
        stack.push(starting_vertex)        # push starting vertex to stack
        while stack.size() > 0:              # while stack is greater than 0,
            current = stack.pop()             # current will be whatever is popped from stack
            if current not in visited:        # if current is not in visited set...
                visited.add(current)          # add current to visited set
                neighbors = self.get_neighbors(current)     # get the neighbors (connections) that current has
                print(f'{current}')       
                for neighbor in neighbors:     # for every neighbor, push them onto the stack (loop keeps going until size reaches 0)
                    stack.push(neighbor)


    def dft_recursive(self, vertex, visited=set()):    # traverse through graph in a depth-first manner (recursively)
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        visited.add(vertex)                         # add vertex to visited
        print(f'{vertex}')
        neighbors = self.get_neighbors(vertex)      # get the neighbors to that vertex
        if len(neighbors) == 0:                     # set up base case to break recursion (when you reach the deepest part)
            return
        for neighbor in neighbors:                  # for every neighbor in neighbors...
            if neighbor not in visited:                 # if that neighbor is not in the visited, then...
                self.dft_recursive(neighbor, visited)       # have the function call itself, except this time the vertex will be that neighbor and visited will be it's current state



    ########## SEARCH ##########


    def bfs(self, starting_vertex, destination):
        """
        Return a list containing the shortest path from
        starting_vertex to destination in
        breath-first order.
        """
        q = Queue()                                              # init queue
        visited  = set()                                         # keep track of visited vertices
        path = [starting_vertex]                                 # start a path array with the first index being our starting vertex
        q.enqueue(path)                                          # enqueue that path to our queue

        while q.size() > 0:                                      # while the size of our queue is greater than 0...
            path = q.dequeue()                                      # path will be whatever vertex is dequeued off our queue
            current_node = path[-1]                                 # current_node will always be the last one in our path array
            if current_node == destination:                         # if current_node is our destination, return path
                return path                                 
            if current_node not in visited:                      # if current_node is not in our visited...
                visited.add(current_node)                           # add that current_node to our visited set
                neighbors = self.get_neighbors(current_node)        # get the neighbors of that current_node
                for neighbor in neighbors:                          # for every neighbor found...
                    path_copy = path[:]                                 # make a copy of our path (so that we don't end up with a vertex we don't need, we want the shortest path)
                    path_copy.append(neighbor)                          # append that neighbor to our copy_path
                    q.enqueue(path_copy)                                # enqueue that path_copy to our queue (what keeps our loop going for as long as we have a path_copy)

    def dfs(self, starting_vertex, destination):
        """
        Return a list containing a path from
        starting_vertex to destination in
        depth-first order.
        """     
        stack = Stack()                                              # init stack
        stack.push([starting_vertex])                                # push starting vertex to stack (as array)
        visited = set()                                              # keep track of visited with a set

        while stack.size() > 0:                                      # while the size of our stack is greater than 0...
            path = stack.pop()                                          # our path will be whatever is popped off our stack (it's an array, remember)
            current_node = path[-1]                                     # current_node will be the last one in our path
            # print(f'CURRENT: {current}')
            if current_node not in visited:                             # if our current_node is not in visited...
                visited.add(current_node)                               # add that current_node to visited set
                if current_node == destination:                         # if our current_node is our destination, return path
                    return path                                             
                neighbors = self.get_neighbors(current_node)            # if current_node is not our destination, then get it's neighbors (assign to variable)
                for neighbor in neighbors:                              # for every neighbor found...
                    path_copy = path[:]                                      # make a path_copy of the current path
                    path_copy.append(neighbor)                               # append that neighbor to path copy
                    stack.push(path_copy)                                    # push path_copy to our stack (keeps our search loop going until current_node is our destination)

    def dfs_recursive(self, vertex, destination, path=[]):
        """
        Return a list containing a path from
        vertex to destination in
        depth-first order.
        This should be done using recursion.
        """
        path = path + [vertex]                                        # path will whatever path currently is + [vertex] (note that first pass will be just that first vertex)

        if vertex == destination:                                     # base case - if our vertex is our destination, return path at that point
            return path                                               
        neighbors = self.get_neighbors(vertex)                        # if our vertex is not what we are looking for, get the neighbors of that vertex...
        for neighbor in neighbors:                                    # for every neighbor in neighbors...
            if neighbor not in path:                                  # if that neighbor is not in our path
                path_copy = self.dfs_recursive(neighbor,destination, path) # create a copy and it'll equal the next recursion of the function, only this time we pass the neighbor, destination, and current state of our path
                if path_copy:                                              # return path_copy if we have one
                    return path_copy

"""
Solving Graph Problems:
    1. Descirbe problem using graph terms:
        -what are our nodes?
        -when are our nodes connected?
        -what are our connected components?
    2. Build our graph or write our get_neighbors():
        -figure out how to get node's edges
    3. Choose algorithm and apply it
"""

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

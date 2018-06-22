# for bfs colors
import random

class Edge:
    # In terms of OOP, this is "overriding" the built in init func
    def __init__(self, destination):
        self.destination = destination

class Vertex:
    # two stars means it will be a list of keyword arguments
    def __init__(self, value, **pos): #TODO: Test default arguments
        self.value = value
        self.color = 'white'
        self.pos = pos
        self.edges = []

class Graph:
    def __init__(self):
        self.vertexes = []
    
    def debug_create_test_data(self):
        
        # ============== HARDCODED VERTS ============== #

        debug_vertex_1 = Vertex('t1', x=400, y=100)
        debug_vertex_2 = Vertex('t2', x=300, y=200)
        debug_vertex_3 = Vertex('t3', x=500, y=100)
        debug_vertex_4 = Vertex('t4', x=600, y=200)
        debug_vertex_5 = Vertex('t5', x=400, y=450)
        debug_vertex_6 = Vertex('t6', x=50, y=100)
        debug_vertex_7 = Vertex('t7', x=50, y=300)
        debug_vertex_8 = Vertex('t8', x=100, y=450)
        debug_vertex_9 = Vertex('t9', x=100, y=250)
        debug_vertex_10 = Vertex('t10', x=300, y=400)
        debug_vertex_11= Vertex('t11', x=300, y=150)
        debug_vertex_12 = Vertex('t12', x=50, y=400)

 
        # ============== HARDCODED EDGES ============== #

        debug_edge_1 = Edge(debug_vertex_2)
        debug_vertex_1.edges.append(debug_edge_1)
     
        # creates new edge 2 with destination vertex 2
        debug_edge_2 = Edge(debug_vertex_3)
        debug_vertex_2.edges.append(debug_edge_2)
     
        debug_edge_3 = Edge(debug_vertex_4)
        debug_vertex_3.edges.append(debug_edge_3)
 
        debug_edge_4 = Edge(debug_vertex_5)
        debug_vertex_4.edges.append(debug_edge_4)
     
        debug_edge_5 = Edge(debug_vertex_6)
        debug_vertex_5.edges.append(debug_edge_5)
        
        debug_edge_6 = Edge(debug_vertex_7)
        debug_vertex_6.edges.append(debug_edge_6)


        self.vertexes.extend([debug_vertex_1,
                              debug_vertex_2, 
                              debug_vertex_3, 
                              debug_vertex_4, 
                              debug_vertex_5, 
                              debug_vertex_6, 
                              debug_vertex_7, 
                              debug_vertex_8, 
                              debug_vertex_9, 
                              debug_vertex_10, 
                              debug_vertex_11, 
                              debug_vertex_12])

    def bfs(self, start):
        random_color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])

        queue = []
        found = []

        queue.append(start)
        found.append(start)

        start.color = random_color

        while len(queue) > 0:
            v = queue[0]
            for edge in v.edges:
                if edge.destination not in found:
                    found.append(edge.destination)
                    queue.append(edge.destination)
                    edge.destination.color = random_color
            # https://stackoverflow.com/questions/4426663/how-to-remove-the-first-item-from-a-list
            queue.pop(0) #TODO: Look into collections.dequeue
        return found

    def get_connected_components(self):
        print("Entering get_connect_components")
        searched = []
        for vertex in self.vertexes:
            if vertex.color == 'white':
                self.bfs(vertex)

#   getConnectedComponents() {
#     let searched = [];
#     for (let vertex of this.vertexes) {
#       if (!searched.includes(vertex)) {
#         searched = searched.concat(this.dfs(vertex));
#       }
#     }
#     // Connected Components:
#     // 1. Go to the next unfound vertex in graph.vertexes and call BFS on it.

#     // 2. Go to step 1 until we get to the end of the array. (Loop)
#     // !!! IMPLEMENT ME
#   }
                                        

         


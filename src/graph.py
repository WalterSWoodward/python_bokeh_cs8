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
        debug_vertex_1 = Vertex('t1', x=40, y=40)
        debug_vertex_2 = Vertex('t2', x=140, y=140)
        debug_vertex_3 = Vertex('t3', x=300, y=400)
        # debug_vertex_4 = Vertex('t4', x=140, y=140)
        # debug_vertex_5 = Vertex('t5', x=140, y=140)
        # print("HI I AM FROM GRAPH.PY!", debug_vertex_1.pos['x'])
        # print("Graph()", Graph())
        # creates edge 1 with destination vertex 2
        debug_edge_1 = Edge(debug_vertex_2)
        # adds edge 1 to vertex 1, making vertex 1 the origin/owner of this edge
        debug_vertex_1.edges.append(debug_edge_1)
 
        # creates new edge 2 with destination vertex 2
        debug_edge_2 = Edge(debug_vertex_2)
        debug_vertex_3.edges.append(debug_edge_2)

        self.vertexes.extend([debug_vertex_1, debug_vertex_2, debug_vertex_3])

# # PICKUP FROM 20-30min left
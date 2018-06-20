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
        print("HI I AM FROM GRAPH.PY!", debug_vertex_1.pos['x'])
        debug_edge_1 = Edge(debug_vertex_2)
        debug_vertex_1.edges.append(debug_edge_1)

        self.vertexes.extend([debug_vertex_1, debug_vertex_2])

# # PICKUP FROM 20-30min left
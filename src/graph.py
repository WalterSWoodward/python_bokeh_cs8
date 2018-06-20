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
        print(debug_vertex_1.pos['x'])

# # PICKUP FROM 20-30min left
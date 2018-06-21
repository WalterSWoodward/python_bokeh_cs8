import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral8

from graph import *

graph_data = Graph()
graph_data.debug_create_test_data()
# print("\ngraph_data.vertexes: \n", graph_data.vertexes, "\n")
# print("\ngraph_data.vertexes[0].edges: \n", graph_data.vertexes[0].edges, "\n")

# Cannot just increase this to get more vertexes
# Bokeh works if you decrease the number though - it will render what it can in
# the case of incomplete data.
N = len(graph_data.vertexes) # makes N dynamic
node_indices = list(range(N))

color_list = []
for vertex in graph_data.vertexes:
    color_list.append(vertex.color)

# debug_pallete += [a, b, c] # Can use this format as well to combine into one line

plot = figure(title='Graph Layout Demonstration', x_range=(0, 500), y_range=(0,500),
              tools='', toolbar_location=None)

graph = GraphRenderer()

# Adds node indices (N of them)
graph.node_renderer.data_source.add(node_indices, 'index')
# Spectral8 is a list of colors
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Oval(height=10, width=10, fill_color='color')

# This is drawing the edges from start to end

start_indexes = []
end_indexes = []


for start_index, vertex in enumerate(graph_data.vertexes):
    for e in vertex.edges:
        start_indexes.append(start_index)
        # cool - works in python to find index of any obj -> `.index`
        end_indexes.append(graph_data.vertexes.index(e.destination))

graph.edge_renderer.data_source.data = dict(
    # This is why all the edges start from the first vertex
    # Creates a list of length N of 0's: [0,0,0]
    start=start_indexes, # This is now [0,1,2]
    # 0 ----- 1
    # 1 ----- 2
    # 2 ----- 2
    end=end_indexes) # TODO: Grab these numbers directly from vertexes

### start of layout code
# Looks like this is setting the positions of the vertexes
x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)
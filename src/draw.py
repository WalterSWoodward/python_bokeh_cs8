import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, Triangle, Diamond
from bokeh.palettes import Spectral8

# Added for labels
from bokeh.plotting import show, output_file
from bokeh.models import ColumnDataSource, Range1d, LabelSet, Label

from graph import *

WIDTH = 640
HEIGHT = 480 #TODO: Currently graph renders square, scaled to numbers here. Possible fix: https://stackoverflow.com/questions/21980662/how-to-change-size-of-bokeh-figure
CIRCLE_SIZE = 30
DIAMOND_SIZE = 40

graph_data = Graph()
graph_data.debug_create_test_data()
graph_data.get_connected_components()
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
# `figure` options: https://bokeh.pydata.org/en/latest/docs/reference/plotting.html
plot = figure(title='Graph Layout Demonstration', x_range=(0, WIDTH), y_range=(0,HEIGHT),
              tools='pan,wheel_zoom,box_zoom,save,reset,help', toolbar_location=None, plot_width=WIDTH, plot_height=HEIGHT)

graph = GraphRenderer()

# Adds node indices (N of them)
graph.node_renderer.data_source.add(node_indices, 'index')
# Spectral8 is a list of colors
graph.node_renderer.data_source.add(color_list, 'color')
# Circle, Oval or whatever you use needs to be imported at top
# Looking up the docs for `Oval bokeh pydata` first, then navigating
# to Circle is probably the most intuitive route to finding this:
# 
# graph.node_renderer.glyph = Circle(size=CIRCLE_SIZE, line_color="#3288bd", fill_color="white", line_width=3)
# graph.node_renderer.glyph = Triangle(size=SHAPE_SIZE, line_color="#99d594", line_width=2, fill_color="lavender")
graph.node_renderer.glyph = Diamond(size=DIAMOND_SIZE, line_color="#1c9099", line_width=2, fill_color='color')

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

# Create a new dictionary to use as a data source, with three lists in it,
# ordered in the same way as vertexes.
# List of x values
# List of y values
# List of labels

#TODO: Possible optimization: We run through this loop three times
value = [v.value for v in graph_data.vertexes]

label_source = ColumnDataSource(data=dict(x=x,
                                          y=y,
                                          v = value))
# For aligning labels, google searched `LabelSet bokeh`, scanned
# through the various keyword options, and found text_align and text_baseline
# `level = 'glyph'` is an inherited property. Googling `bokeh (+code)` got me
# this: http://bokeh.pydata.org/en/0.11.1/docs/reference/models/renderers.html
# options are: ‘image’, ‘underlay’, ‘glyph’, ‘annotation’, ‘overlay’, ‘tool’
labels = LabelSet(x='x', y='y', text='v', level='overlay',
              x_offset=None, y_offset=None, source=label_source, render_mode='canvas', text_align='center', text_baseline='middle')


#TODO: Investiagete plot.add_layout vs. plot.renderers.append
plot.add_layout(labels)

output_file('graph.html')
show(plot)
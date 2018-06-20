import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral8

# Cannot just increase this to get more vertexes
# Bokeh works if you decrease the number though - it will render what it can in
# the case of incomplete data.
N = 9
node_indices = list(range(N))

# QUESTION: What is this??? - REVIEW
# You cannot mutate Spectral8 directly, so you have to have two lines here.
debug_pallete = Spectral8
debug_pallete.append('#ff0000') # Just adds this color to the list of Spectral8 colors
# debug_pallete.append('#ff0000')
# debug_pallete += [a, b, c] # Can use this format as well to combine into one line

plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,1.1), y_range=(-1.1,1.1),
              tools='', toolbar_location=None)

graph = GraphRenderer()

# Adds node indices (N of them)
graph.node_renderer.data_source.add(node_indices, 'index')
# Spectral8 is a list of colors
graph.node_renderer.data_source.add(debug_pallete, 'color')
graph.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color='color')

graph.edge_renderer.data_source.data = dict(
    start=[0]*N,
    end=node_indices)

### start of layout code
# Looks like this is setting the positions of the vertexes
circ = [i*2*math.pi/N for i in node_indices]
x = [math.cos(i) for i in circ]
y = [math.sin(i) for i in circ]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)
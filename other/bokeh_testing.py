"""
Goal: cloud of points with a slider
"""

# First, need to learn to make circles of different sizes

# Data handling
import pandas as pd
import numpy as np

# Bokeh libraries
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel, Slider
from bokeh.models import HoverTool
from bokeh.models import CustomJS, RangeSlider



# Prepare the data


# Set up the figure(s)
fig = figure()

x = [1,2,3]
y = [1,2,3]
widths = [10,20,30]
colors = ['green', 'red', 'blue']

fig.circle(x=x,y=y,color=colors, size=10, alpha=0.5, width = widths)
fig.grid.grid_line_color = None
fig.axis.visible = False

# Format the tooltip for the hovering interactivity
tooltips = [
            ('Player','@name'),
            ('Three-Pointers Made', '@play3PM'),
            ('Three-Pointers Attempted', '@play3PA'),
            ('Three-Point Percentage','@pct3PM{00.0%}'),
           ]

# Add the HoverTool to the figure
fig.add_tools(HoverTool(tooltips=tooltips))

slider = Slider(start=1, end=11, value=3, step=1, title="Number of disciplines")

slider_code = '''   s = slider_slope.value; '''

slider_callback = CustomJS(args = dict(slider = slider), code = slider_code)

w = slider.value
print(w)


circ = figure()
circ.circle(x = 1, y = 1, color ='green', size = w*10, width = 10)
circ.grid.grid_line_color = None
circ.axis.visible = False


layout = column(slider, circ)
# Determine where the visualization will be rendered
output_file('bokeh_testing.html', title='Testing the bokeh library for hyperViz')  # Render to static HTML, or 
# output_notebook()  # Render inline in a Jupyter Notebook



show(layout)
# TODO: learn how to make this slider actually influence the code
# TODO: basic circle drawing: different sizes, colors, and with labels inside
# TODO: depending on the position of the slider, automatically show the relevant circles

# Connect to and draw the data

# Organize the layout

# Preview and save 
# show(fig)
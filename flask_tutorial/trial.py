

import numpy as np

from bokeh import events
from bokeh.io import output_file, show
from bokeh.layouts import column, row
from bokeh.models import Button, CustomJS, Div,Slider
from bokeh.plotting import figure


def display_event(div):
    """
    Function to build a suitable CustomJS to display the current event
    in the div model.
    """
    style = 'float: left; clear: left; font-size: 13px'
    return CustomJS(code="""
			<h1> the position in {{cb_obj}} </h1>
    """ )


# Add a div to display events and a button to trigger button click events
slider = Slider(title="title",value= 0,start=0,end=30)
div = Div(width=1000)
button = Button(label="Button", button_type="success", width=300)
layout = column(button, row(slider, div))


# Ranges Update events
slider.js_on_change('value', display_event(div))

# # Selection events
# p.js_on_event(events.SelectionGeometry, display_event(div, attributes=['geometry', 'final']))

output_file("js_events.html", title="JS Events Example")
show(layout)

from flask import Flask, render_template
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.models import Slider
from bokeh.resources import INLINE


app = Flask(__name__)



@app.route('/', methods=['GET'])
def bokeh():
    slider = Slider(title = "position",value=0,start=0,end=10)

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(slider)

    html = render_template(
        'index.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources
    )
    return html


if __name__ == '__main__':
    app.run(debug=True)
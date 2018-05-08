from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html

from .dash_server import app
from . import dash_router


app.layout = html.Div(children=[
                                dcc.Location(id='url', refresh=False),
                                html.Div(id='dash_content')
                            ])

# callbacks could go here, or in another callback.py file with this at the top:
# from .server import app

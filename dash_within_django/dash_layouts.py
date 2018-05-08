from random import randint
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

from .models import Author
from django.shortcuts import get_object_or_404


def dash_django_page(pathname):
    ''' '''

    # Here we extract context from the url in order to render relevant data:
    pathelements = pathname.split('/')
    for count, element in enumerate(pathelements):
        if element == 'dash_django_page':
            break
    record_id = pathelements[count-1]

    author = get_object_or_404(Author, pk=record_id)

    message = html.P("From the URL, I am record: %s. This corresponds to author: %s. Info relevant to this record can be extracted\
                       from a database" %(record_id, author.name))



    # Create random data with numpy
    N = 100
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N)+5
    random_y1 = np.random.randn(N)
    random_y2 = np.random.randn(N)-5

    trace1 = go.Scatter(
        x = random_x,
        y = random_y1,
        mode = 'lines+markers',
        name = 'lines+markers'
    )

    data = [trace1]

    layout = dict(title = 'Data',
              yaxis = dict(zeroline = False),
              xaxis = dict(zeroline = False)
             )

    fig = dict(data=data, layout=layout)

    graph = dcc.Graph(id='main-graph', figure=fig, style={'display':'inline-block'} )



    page_layout = html.Div(children=[message, html.Div(children=[dcc.Dropdown(id='dropdown', className='dropdown',
                                                                                options=[{'label': i, 'value': i} for i in ['option1', 'option2', 'option3']],
                                                                                value='option1',
                                                                                 ),
                                                                ]), # end of dropdown div
                                      graph,]), # end of page_layout_div

    return page_layout


def someotherpage(pathname):
    ''' '''
    return html.P('hello world! I am "someotherpage"')

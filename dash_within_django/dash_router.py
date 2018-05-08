from dash.dependencies import Output, Input

from .dash_server import app, server
from . import dash_layouts
from . import urls

# Define a dictionary of the pages in the urlpatterns that you wish to associate Dash.
# Dash will match what is in the url to the keys in this dictionary and return the corresponding layout
dash_routes = (
                ('dash_django_page', dash_layouts.dash_django_page),
                ('someotherpage', dash_layouts.someotherpage),
               )

dash_routes = dict(dash_routes)

@app.callback(Output('dash_content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    ''' '''

    if pathname is None:
        return ''

    print("\n\nPrinting pathname:%s" %(pathname) )
    print("Printing dash url routes:")
    for k, v in dash_routes.items():
        if k in pathname:
            page = dash_routes[k]
            print("\tCurrent key: '%s' has a page matched. Returning the corresponding layout" %(k))
        else:
            print("\tCurrent key: '%s' has no page match" %(k))
    print("\n\n")

    if callable(page):
        layout = page(pathname)
    else:
        layout = page

    return layout

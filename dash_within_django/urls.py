from django.urls import path, re_path
from . import views

from . import dash_app_base_generic # this loads the Dash app
from . import dash_layouts
from .dash_server import app, server


app_name = 'dash_within_django'

urlpatterns = [
                re_path('^_dash-', views.dash_ajax),

                path('index/', views.index, name='index'),
                path('<author_id>/dash_django_page/', views.dash_django_page, name='dash-django-page'),

              ]

# Django related imports:
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Author

# Dash related imports:
from .dash_server import dash_dispatcher, clean_dash_content
from django.views.decorators.csrf import csrf_exempt


def index(request):

    # get the list of engagements:
    authors = Author.objects.all()

    # get dash content:
    print("Function: index()")

    context = {'authors':authors}

    return render(request, 'dash_within_django/index.html', context=context)

@csrf_exempt
def dash_ajax(request, **kwargs):
    print('Function: dash_ajax')
    return HttpResponse(dash_dispatcher(request,), content_type='application/json')

def dash_django_page(request, author_id):

    # get the django context:
    author = get_object_or_404(Author, pk=author_id)

    print("Function: dash_django_page(): Getting 'dash_content'")
    dash_content = HttpResponse(dash_dispatcher(request,), content_type='application/json').getvalue()
    # clean the dash html content (the content contains lots of unnecessary characters like '\n')
    dash_content = clean_dash_content(dash_content)
    context = {'author':author, 'dash_content': dash_content}

    return render(request, 'dash_within_django/dash_django_page.html', context=context)

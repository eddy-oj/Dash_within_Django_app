from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    #admin
    path('admin/', admin.site.urls),

    # app:
    path('dash_within_django/', include('dash_within_django.urls')),

    # end of urls list. append static doc folder:
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

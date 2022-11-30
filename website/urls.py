from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.views.static import serve
from django.urls import re_path as url
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap

sitemaps = {'static': StaticViewSitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('gallery/', include('gallery.urls')),
    path('contactus/', include('contactus.urls')),
    path('tours/', include('tours.urls')),
    path('cars/', include('cars.urls')),
    path('aboutus/', include('aboutus.urls')),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),

    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT})
]
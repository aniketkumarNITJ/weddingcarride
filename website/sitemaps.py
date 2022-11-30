from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return ['home', 'aboutus', 'tours', 'gallery', 'contactus']

    def location(self, item):
        return reverse(item)

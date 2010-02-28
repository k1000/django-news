from django.contrib.syndication.feeds import Feed
from models import News

class LatestEntries(Feed):
    title = u"CTECA - últimas Noticias"
    link = "/news/"
    description = "Noticias de CTECA.es"

    def items(self):
        return News.objects.get_published().order_by('-pub_date')[:5]
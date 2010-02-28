from datetime import datetime

from django.template.context import RequestContext
from django.views.generic import list_detail
from django.shortcuts import render_to_response

from news.models import News, Section


def index(request):
    articles = News.objects.get_published()[:5]
    try:
        from photologue.models import Gallery
        galleries = Gallery.objects.all()[:3]
    except:
        pass
    return render_to_response('news/index.html', locals(),
                              context_instance=RequestContext(request))


def view_section(request, slug, page=1):
    section = News.objects.get(slug__exact=slug)
    articles = section.articles.filter(publish=True, pub_date__lte=datetime.now())

    return list_detail.object_list(request,
                                   queryset=articles,
                                   paginate_by=5,
                                   page=page,
                                   allow_empty=True,
                                   template_name='news/view_section.html',
                                   extra_context={'section': section, )

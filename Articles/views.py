from django.http import HttpResponse
from django.template import RequestContext, loader
from Articles.models import Article, Image


def index(request):
    last_articles = Article.objects.order_by('-create_date')[:5]
    backgrounds = Image.objects.order_by('fileInfo')[:1]
    template = loader.get_template('index.html')

    context = RequestContext(request, {
        'last_articles': last_articles,
        'backgrounds': backgrounds
    })
    return HttpResponse(template.render(context))



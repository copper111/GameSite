from django.http import HttpResponse
from django.template import RequestContext, loader
from Articles.models import Article, Image
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def articles(request):
    last_articles = Article.objects.order_by('-create_date')[:5]
    backgrounds = Image.objects.order_by('fileInfo')[:1]
    return render(request, 'articles.html', {
        'last_articles': last_articles,
        'backgrounds': backgrounds
    })




from Articles.models import Article, Image
from django.shortcuts import render


def articles(request):
    last_articles = Article.objects.order_by('-create_date')[:5]
    backgrounds = Image.objects.order_by('fileInfo')[:1]
    return render(request, 'articles.html', {
        'last_articles': last_articles,
        'backgrounds': backgrounds
    })




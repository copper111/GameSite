from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from Articles import views

urlpatterns = patterns('',
    url(r'^articles/', views.articles, name='articles'),
    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

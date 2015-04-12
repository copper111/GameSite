__author__ = 'artpg'
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from GamesHistory import views

urlpatterns = patterns('',
    url(r'^gameshistory/', views.gameshistory, name='gameshistory'),
    url(r'^searchsummoner/', views.searchsummoner, name='searchsummoner'),
    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
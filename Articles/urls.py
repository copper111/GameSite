from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings

from Articles import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

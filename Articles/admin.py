from django.contrib import admin
from Articles.models import Article, Image, Champion
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
     list_display = ('article', 'create_date')



class ChampionAdmin(admin.ModelAdmin):
     list_display = ('champion', 'spec_id')

class ArticleImage(admin.ModelAdmin):
     list_display = ('file', 'fileInfo')




admin.site.register(Article, ArticlesAdmin)
admin.site.register(Champion, ChampionAdmin)
admin.site.register(Image, ArticleImage)

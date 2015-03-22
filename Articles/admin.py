from django.contrib import admin
from Articles.models import Article, Game, Champion
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
     list_display = ('article', 'create_date')


class ChampionAdmin(admin.ModelAdmin):
     list_display = ('champion', 'spec_id')


admin.site.register(Article, ArticlesAdmin)
admin.site.register(Champion, ChampionAdmin)

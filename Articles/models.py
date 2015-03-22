from django.db import models

# Create your models here.
class Champion (models.Model):
    champion = models.CharField(max_length=200)
    spec_id = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.champion

class Game(models.Model):
    game = models.CharField(max_length=200)

class Article (models.Model):
    champion = models.ForeignKey(Champion)
    # champion = models.CharField(max_length=300)
    article = models.CharField(max_length=300)
    article_text = models.TextField(default='')
    create_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.article

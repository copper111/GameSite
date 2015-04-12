__author__ = 'artpg'

from django.shortcuts import render
from django.http import HttpResponse


def searchsummoner(request):
    return render(request, 'searchsummoner.html'
    )

def gameshistory(request):
    if 'summoner' in request.GET:
        summoner_name = request.GET['summoner']
    else:
        summoner_name = 'You submitted an empty form.'
    return render(request, 'gameshistory.html', {
        'summoner_name': summoner_name}
    )

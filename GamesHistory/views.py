__author__ = 'artpg'

from django.shortcuts import render
from riotwatcher import RiotWatcher


def searchsummoner(request):
    return render(request, 'searchsummoner.html'
    )

def gameshistory(request):
    if ('summoner' in request.GET):
        summoner_name = request.GET['summoner']
        region = request.GET['region']
    else:
        summoner_name = 'You submitted an empty form.'

    w = RiotWatcher('12934b95-1914-42bc-b092-208bb64c7793')
    me = w.get_summoner(name=summoner_name, region=region)
    mh = w.get_match_history(me['id'], region=region, begin_index=14, end_index=15)


    return render(request, 'gameshistory.html', {
        'summoner_name': summoner_name, 'gson': me, 'mh':mh}
    )

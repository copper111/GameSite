__author__ = 'artpg'

from django.shortcuts import render
from riotwatcher import RiotWatcher
import json


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
    mh = w.get_match_history(me['id'], region=region, begin_index=1, end_index=3)
    # print mh
    f = open('D:\\Projects\\ddragon\\dragontail-5.7.2\\5.7.2\data\\ru_RU\\champion.json', 'r').read()

    j = json.loads(f)

    champNameCollection = set()

    for match in  mh['matches']:
        # print match['queueType']
        for champ in match['participants']:
            for champName in j['data']:
                if int(j['data'][champName]['key']) == int(champ['championId']):
                    # champNameCollection = j['data'][champName]['id']
                    print j['data'][champName]['id']
                    champNameCollection.add(j['data'][champName]['id'])



    return render(request, 'gameshistory.html', {
        'summoner_name': summoner_name, 'gson': me, 'mh':mh, 'champNameCollection': champNameCollection}
    )

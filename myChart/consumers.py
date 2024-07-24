import json
from asyncio import sleep
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from myChart.models import *


def voteCount(candi):
    voteCount = voter.objects.filter(vote=candi).count()
    return voteCount

class ChartConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
        while True:
            trumpVote = voteCount('TRUMP')
            harrisVote = voteCount('HARRIS')
            joeVote = voteCount('JOE')
            obamaVote = voteCount('OBAMA')
            mikeVote = voteCount('MIKE')
            kennedyVote = voteCount('KENNEDY')
            westVote = voteCount('WEST')
            oliverVote = voteCount('OLIVER')
            halleyVote = voteCount('HALLEY')
            noVote = voteCount('NO VOTE')
            
            await self.send(json.dumps({
                'trump': trumpVote,
                'mike': mikeVote,
                'halley': halleyVote,
                'joe': joeVote,
                'obama': obamaVote,
                'harris': harrisVote,
                'kennedy': kennedyVote,
                'west': westVote,
                'oliver': oliverVote,
                'no': noVote
            }))
            
            await sleep(2)
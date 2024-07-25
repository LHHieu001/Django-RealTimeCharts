import json

from asyncio import sleep
from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.db import database_sync_to_async
from myChart.models import *
from asgiref.sync import sync_to_async




class ChartConsumer(AsyncWebsocketConsumer):
    
    def voteCount(self, candi):
        voteCount = voter.objects.filter(vote=candi).count()
        return voteCount

    async def connect(self):
        await self.accept()
        
        while True:
            trumpVote = await sync_to_async(self.voteCount)('TRUMP')
            harrisVote = await sync_to_async(self.voteCount)('HARRIS')
            joeVote = await sync_to_async(self.voteCount)('JOE')
            obamaVote = await sync_to_async(self.voteCount)('OBAMA')
            mikeVote = await sync_to_async(self.voteCount)('MIKE')
            kennedyVote = await sync_to_async(self.voteCount)('KENNEDY')
            westVote = await sync_to_async(self.voteCount)('WEST')
            oliverVote = await sync_to_async(self.voteCount)('OLIVER')
            halleyVote = await sync_to_async(self.voteCount)('HALLEY')
            noVote = await sync_to_async(self.voteCount)('NO VOTE')
            
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
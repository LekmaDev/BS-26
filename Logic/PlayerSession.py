from Server.Battle.VisionUpdate import VisionUpdate
from Server.Battle.StartLoadingMessage import StartLoadingMessage
from Server.Battle.UDPConnectionInfo import UDPConnectionInfo
import time
from threading import Thread
from Utils.MatchmakingLogic import MatchmakingLogic
class PlayerSession(Thread):
    def __init__(self, client, player):
        Thread.__init__(self)
        self.client = client
        self.player = player
        self.started = 0
        self.matchmaker = MatchmakingLogic()
        self.my_battle = self.matchmaker.get_battle_for_id(self.player.battleID)
    
    def run(self):
        self.startBattle()
    
    def startBattle(self):
        self.started = 1
        StartLoadingMessage(self.client, self.player, self.my_battle).send()
        UDPConnectionInfo(self.client, self.player).send()
        while self.started:
            self.my_battle["battleTick"] += 1
            if self.my_battle["battleTick"] > 2530:
                self.started = 0
            self.process()
            time.sleep(0.15) 

    def process(self):
        VisionUpdate(self.client, self.player, self.my_battle).send()
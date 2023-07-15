from Server.Battle.MatchmakeCancelledMessage import MatchmakeCancelledMessage
from Utils.Reader import BSMessageReader
from Utils.MatchmakingLogic import MatchmakingLogic

class CancelMatchMaking(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        pass

    def process(self):
        matchmaker = MatchmakingLogic()
        matchmaker.Leave_Battle(self.player.battleID,self.player.low_id)
        self.player.inmm = False
        MatchmakeCancelledMessage(self.client, self.player).send()
from Server.Battle.MatchmakingInfoMessage import MatchmakingInfoMessage
from Utils.Reader import BSMessageReader
from Utils.MatchmakingLogic import MatchmakingLogic
from Files.CsvLogic.Cards import Cards
class OnPlay(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
    def decode(self):
        pass

    def process(self):
        matchmaker = MatchmakingLogic()
        maxhp = Cards.get_brawler_hp(self.player.brawler_id+1)
        matchmaker.check(self.player.low_id,self.player.brawler_id,self.player.skin_id,maxhp)
        battles = matchmaker.get_battles()
        for battle in battles:
            for player in battle["players"]:
                if player["plrID"] == self.player.low_id:
                    self.player.battleID = battle["id"]
                    self.player.inmm = True
        my_battle = matchmaker.get_battle_for_id(self.player.battleID)
        for i in my_battle["players"]:
            MatchmakingInfoMessage(self.client, self.player).sendWithLowID(i["plrID"])
from Utils.BitStream import BitStream
from Utils.Helpers import Helpers
from Utils.Writer import Writer 
import random
from Logic.Battle.Objects.LogicCharacterServer import LogicCharacterServer
from Logic.Battle.Objects.LogicProjectileServer import LogicProjectileServer
from Logic.Battle.Component.LogicRespawn import LogicRespawn
class GameObjectManager:
    def encode(stream,my_battle, self):
        self.my_battle = my_battle

        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(1, 1)

        stream.writePositiveInt(0, 5)
        stream.writePositiveInt(0, 6)
        stream.writePositiveInt(0, 5)
        stream.writePositiveInt(0, 6)

        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(0, 1)
        stream.writeBoolean(False)

        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 12)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        
        stream.writePositiveInt(1, 1)

        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)

        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)

        stream.writePositiveInt(1, 1)
        stream.writePositiveVIntMax255(int(self.my_battle["players"][0]["stars"]))#Team Blu Gem int(self.my_battle["battleTick"]/45)
        stream.writePositiveInt(0, 1)

        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)

        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)

        stream.writePositiveInt(1, 1)
        stream.writePositiveVIntMax255(int(self.my_battle["players"][1]["stars"]))#Team red Gem int(self.my_battle["battleTick"]/45)
        stream.writePositiveInt(0, 1)

        stream.writePositiveInt(0, 4)
        stream.writePositiveInt(int(self.my_battle["GameObjeckCount"])+len(self.my_battle["LogicItem"]), 7)
        LogicProjectileServer.data(stream,self.my_battle,self)
        if self.my_battle["players"][0]["plrID"] == self.player.low_id:
            stream.writePositiveInt(16, 5)
            stream.writePositiveInt(int(self.my_battle["players"][0]["BID"]), 8)
            stream.writePositiveInt(16, 5)
            stream.writePositiveInt(int(self.my_battle["players"][1]["BID"]), 8)
        elif self.my_battle["players"][1]["plrID"] == self.player.low_id:
            stream.writePositiveInt(16, 5)
            stream.writePositiveInt(int(self.my_battle["players"][1]["BID"]), 8)
            stream.writePositiveInt(16, 5)
            stream.writePositiveInt(int(self.my_battle["players"][0]["BID"]), 8)
        for i in range(len(self.my_battle["LogicItem"])):
            stream.writePositiveInt(i, 14)
        stream.writePositiveInt(0, 14)
        stream.writePositiveInt(5, 14)
        LogicProjectileServer.encode(stream,self.my_battle,self)
        LogicRespawn.Health(stream,self.my_battle,self)
        LogicRespawn.Respawn(stream,self.my_battle,self)
        LogicCharacterServer.encode(stream,self.my_battle,self)
        self.writeBytes(stream.getBuff())
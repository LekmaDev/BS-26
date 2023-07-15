from Utils.Writer import Writer
from Utils.BitStream import BitStream

class LogicCharacterServer:
    def encode(stream,my_battle,self):
        self.my_battle = my_battle
        if self.my_battle["players"][0]["plrID"] == self.player.low_id:
            stream.writePositiveVInt(int(self.my_battle["players"][0]["plrX"]), 4)
            stream.writePositiveVInt(int(self.my_battle["players"][0]["plrY"]), 4)
            stream.writePositiveVInt(0, 3)
            stream.writePositiveVInt(0, 4)
            stream.writePositiveInt(10, 4)
            stream.writePositiveInt(0, 1)#isownobj
            stream.writePositiveInt(0, 3)
            stream.writePositiveInt(0, 1)
            stream.writeInt(63, 6)
            stream.writePositiveInt(0, 1)#дёргает и не rotate
            stream.writePositiveInt(0, 1)#stan
            stream.writePositiveInt(0, 1)#unk
            stream.writePositiveInt(0, 1)#star power indicator
            stream.writePositiveInt(1, 1)#1
            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(0, 2)
            stream.writePositiveInt(int(self.my_battle["players"][0]["hp"]), 13)
            stream.writePositiveInt(int(self.my_battle["players"][0]["maxhp"]), 13)
            stream.writePVIntMax255OZ(int(self.my_battle["players"][0]["stars"]))
            stream.writePVIntMax255OZ(0)
            stream.writePositiveInt(0, 1)#is owner
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(0, 4)
            stream.writePositiveInt(0, 2)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(0, 9)
            stream.writePositiveInt(0, 1)#is owner
            stream.writePositiveInt(0, 1)#is owner
            stream.writePositiveInt(0, 5)
            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(int(self.my_battle["players"][0]["charge"]), 12)
            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(1, 1)
            
            stream.writePositiveVInt(int(self.my_battle["players"][1]["plrX"]), 4)#
            stream.writePositiveVInt(int(self.my_battle["players"][1]["plrY"]), 4)#
            stream.writePositiveVInt(4, 3)
            stream.writePositiveVInt(0, 4)
            stream.writePositiveInt(10, 4)
            stream.writePositiveInt(int(self.my_battle["players"][1]["angle"]), 9)#isownobj
            stream.writePositiveInt(int(self.my_battle["players"][1]["angle"]), 9)#isownobj
            stream.writePositiveInt(0, 3)
            stream.writePositiveInt(0, 1)
            stream.writeInt(63, 6)
            stream.writePositiveInt(0, 1)#дёргает и не rotate
            stream.writePositiveInt(0, 1)#stan
            stream.writePositiveInt(0, 1)#unk
            stream.writePositiveInt(0, 1)#star power indicator
            stream.writePositiveInt(1, 1)#1
            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(0, 2)
            stream.writePositiveInt(int(self.my_battle["players"][1]["hp"]), 13)
            stream.writePositiveInt(int(self.my_battle["players"][1]["maxhp"]), 13)
            stream.writePVIntMax255OZ(int(self.my_battle["players"][1]["stars"]))
            stream.writePVIntMax255OZ(0)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(0, 4)
            stream.writePositiveInt(0, 2)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(0, 9)
            stream.writePositiveInt(0, 5)
            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(int(self.my_battle["players"][1]["charge"]), 12)
            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(1, 1)
        elif self.my_battle["players"][1]["plrID"] == self.player.low_id:
            stream.writePositiveVInt(int(self.my_battle["players"][1]["plrX"]), 4)#
            stream.writePositiveVInt(int(self.my_battle["players"][1]["plrY"]), 4)#
            stream.writePositiveVInt(4, 3)
            stream.writePositiveVInt(0, 4)
            stream.writePositiveInt(10, 4)
            stream.writePositiveInt(0, 1)#isownobj
            stream.writePositiveInt(0, 3)
            stream.writePositiveInt(0, 1)
            stream.writeInt(63, 6)
            stream.writePositiveInt(0, 1)#дёргает и не rotate
            stream.writePositiveInt(0, 1)#stan
            stream.writePositiveInt(0, 1)#unk
            stream.writePositiveInt(0, 1)#star power indicator
            stream.writePositiveInt(1, 1)#1
            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(0, 2)
            stream.writePositiveInt(int(self.my_battle["players"][1]["hp"]), 13)
            stream.writePositiveInt(int(self.my_battle["players"][1]["maxhp"]), 13)
            stream.writePVIntMax255OZ(int(self.my_battle["players"][1]["stars"]))
            stream.writePVIntMax255OZ(0)
            stream.writePositiveInt(0, 1)#is owner
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(0, 4)
            stream.writePositiveInt(0, 2)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(0, 9)
            stream.writePositiveInt(0, 1)#is owner
            stream.writePositiveInt(0, 1)#is owner
            stream.writePositiveInt(0, 5)
            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(int(self.my_battle["players"][1]["charge"]), 12)
            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(1, 1)
            
            stream.writePositiveVInt(int(self.my_battle["players"][0]["plrX"]), 4)#
            stream.writePositiveVInt(int(self.my_battle["players"][0]["plrY"]), 4)#
            stream.writePositiveVInt(0, 3)
            stream.writePositiveVInt(0, 4)
            stream.writePositiveInt(10, 4)
            stream.writePositiveInt(int(self.my_battle["players"][0]["angle"]), 9)#isownobj
            stream.writePositiveInt(int(self.my_battle["players"][0]["angle"]), 9)#isownobj
            stream.writePositiveInt(0, 3)
            stream.writePositiveInt(0, 1)
            stream.writeInt(63, 6)
            stream.writePositiveInt(0, 1)#дёргает и не rotate
            stream.writePositiveInt(0, 1)#stan
            stream.writePositiveInt(0, 1)#unk
            stream.writePositiveInt(0, 1)#star power indicator
            stream.writePositiveInt(1, 1)#1
            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(0, 2)
            stream.writePositiveInt(int(self.my_battle["players"][0]["hp"]), 13)
            stream.writePositiveInt(int(self.my_battle["players"][0]["maxhp"]), 13)
            stream.writePVIntMax255OZ(int(self.my_battle["players"][0]["stars"]))
            stream.writePVIntMax255OZ(0)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(0, 4)
            stream.writePositiveInt(0, 2)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(0, 9)
            stream.writePositiveInt(0, 5)
            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(int(self.my_battle["players"][0]["charge"]), 12)
            stream.writePositiveInt(1, 1)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(1, 1)
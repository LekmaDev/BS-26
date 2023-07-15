from Utils.Writer import Writer
from Utils.BitStream import BitStream
import math
class LogicProjectileServer:
    def encode(stream,my_battle,self):
        self.my_battle = my_battle
        for data in self.my_battle["LogicItem"]:
            stream.writePositiveVInt(int(data[0]["x"]), 4)
            stream.writePositiveVInt(int(data[0]["y"]), 4)
            stream.writePositiveVInt(0, 3)
            stream.writePositiveVInt(450, 4)
            stream.writePositiveInt(0, 3)
            stream.writePositiveInt(0, 1)
            stream.writePositiveInt(275, 10)#IsBouncing
            stream.writePositiveInt(int(data[0]["angle"]), 9)
            stream.writePositiveInt(0, 1)
            data[0]["Tick"] += 1
        for data in self.my_battle["LogicItem"]:
            if data[0]["Tick"] >= 35:
                self.my_battle["LogicItem"].remove(data)
            else:
                if data[0]["y"] < 0:
                    self.my_battle["LogicItem"].remove(data)
                elif data[0]["x"] < 0:
                    self.my_battle["LogicItem"].remove(data)
                radius = 256
                distance = math.sqrt((data[0]["x"] - self.my_battle["players"][0]["plrX"]) ** 2 + (data[0]["y"] - self.my_battle["players"][0]["plrY"]) ** 2)
                distance2 = math.sqrt((data[0]["x"] - self.my_battle["players"][1]["plrX"]) ** 2 + (data[0]["y"] - self.my_battle["players"][1]["plrY"]) ** 2)
                if distance <= radius:
                    if data[0]["sender"] != self.my_battle["players"][0]["plrID"]:
                        self.my_battle["LogicItem"].remove(data)
                        self.my_battle["players"][0]["hp"] = int(self.my_battle["players"][0]["hp"]) - 250
                if distance2 <= radius:
                    if data[0]["sender"] != self.my_battle["players"][1]["plrID"]:
                        self.my_battle["LogicItem"].remove(data)
                        self.my_battle["players"][1]["hp"] = int(self.my_battle["players"][1]["hp"]) - 250
                if data[0]["x"] < data[0]["x"]+data[0]["x"]+data[0]["ToX"] or data[0]["y"] < data[0]["y"]+data[0]["y"]+data[0]["ToY"]:
                    data[0]["x"] = data[0]["x"]+data[0]["ToX"]//12
                    data[0]["y"] = data[0]["y"]+data[0]["ToY"]//12
                    if data[0]["y"] < 0:
                        self.my_battle["LogicItem"].remove(data)
                    elif data[0]["x"] < 0:
                        self.my_battle["LogicItem"].remove(data)
    def data(stream,my_battle,self):
        self.my_battle = my_battle
        for data in self.my_battle["LogicItem"]:
            stream.writePositiveInt(6, 5)
            stream.writePositiveInt(int(data[0]["id"]), 8)
    def SpawnBullet(BID,self):
        pass
		#return 0
    def getItem(brawlerID,self):
        id = 0
        if brawlerID == 0:#shelly
            id = 6
        elif brawlerID == 1:#kolt
            id = 8
        elif brawlerID == 2:#bull
            id = 2
        elif brawlerID == 3:#brock
            id = 15
        elif brawlerID == 4:#rico
            id = 12
        elif brawlerID == 5:#spike
            id = 29
        elif brawlerID == 6:#barrly
            id = 6
        elif brawlerID == 7:#jessy
            id = 8
        elif brawlerID == 8:#nita
            id = 2
        elif brawlerID == 9:#dino
            id = 8
        elif brawlerID == 10:#el primo
            id = 8
        elif brawlerID == 12:#croy
            id = 8
        elif brawlerID == 13:#poko
            id = 2
        elif brawlerID == 14:#Bo
            id = 8
        elif brawlerID == 15:#paper
            id = 8
        elif brawlerID == 16:#pem
            id = 29
        elif brawlerID == 17:#tara
            id = 6
        elif brawlerID == 18:#derrly
            id = 8
        elif brawlerID == 19:#peny
            id = 2
        elif brawlerID == 20:#frank
            id = 8
        elif brawlerID == 21:#gene
            id = 8
        elif brawlerID == 22:#tick
            id = 29
        elif brawlerID == 23:#leon
            id = 8
        elif brawlerID == 24:#rosa
            id = 2
        elif brawlerID == 25:#karl
            id = 8
        elif brawlerID == 26:#bibi
            id = 8
        elif brawlerID == 27:#8-bit
            id = 29
        elif brawlerID == 28:#sendy
            id = 6
        elif brawlerID == 29:#bia
            id = 8
        elif brawlerID == 30:#emz
            id = 2
        elif brawlerID == 31:#m.pi
            id = 8
        elif brawlerID == 32:#maks
            id = 8
        elif brawlerID == 34:#jeky
            id = 29
        elif brawlerID == 34:#sprout
            id = 29
        return id
class LogicRespawn:
    def Health(stream,my_battle,self):
        self.my_battle["players"][0]["charge"] = min(int(self.my_battle["players"][0]["charge"]) + 15, 3000)
        self.my_battle["players"][1]["charge"] = min(int(self.my_battle["players"][1]["charge"]) + 15, 3000)
        #if int(self.my_battle["players"][0]["hp"]) < int(self.my_battle["players"][0]["maxhp"]):
        #    self.my_battle["players"][0]["hp"] = int(self.my_battle["players"][0]["hp"]) + 2
        #if int(self.my_battle["players"][1]["hp"]) < int(self.my_battle["players"][1]["maxhp"]):
        #    self.my_battle["players"][1]["hp"] = int(self.my_battle["players"][1]["hp"]) + 2
    def Respawn(stream,my_battle,self):
        if int(self.my_battle["players"][0]["hp"]) <= 50:
            self.my_battle["players"][0]["plrX"] = 3125
            self.my_battle["players"][0]["plrY"] = 9500
            self.my_battle["players"][0]["hp"] = self.my_battle["players"][0]["maxhp"]
            self.my_battle["players"][1]["stars"] = int(self.my_battle["players"][1]["stars"]) + 1
        if int(self.my_battle["players"][1]["hp"]) <= 50:
            self.my_battle["players"][1]["plrX"] = 3125
            self.my_battle["players"][1]["plrY"] = 1200
            self.my_battle["players"][1]["hp"] = self.my_battle["players"][1]["maxhp"]
            self.my_battle["players"][0]["stars"] = int(self.my_battle["players"][0]["stars"]) + 1
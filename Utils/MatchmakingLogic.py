class MatchmakingLogic:
    MaxPlayer = 2
    battles = [
        {
            "id": 1,
            "GameObjeckCount": 2,
            "LogicItem": [],
            "killlist": [],
            "battleTick": 0,
            "battleStart": False,
            "players": []
        }
    ]

    def get_battles(self):
        return self.battles
    def check(self,ID,BID,SID,maxhp):
        # Find battles that are not full and have not started
        eligible_battles = [battle for battle in self.battles if len(battle["players"]) < self.MaxPlayer and not battle["battleStart"]]

        if len(eligible_battles) > 0:
            # If there are eligible battles, add the player to the first one
            new_player = {"plrID": ID, "plrX": 3125, "plrY": 9500,"angle":270,"BID": BID,"SID":SID,"maxhp":maxhp,"hp":maxhp,"stars":0,"charge":3000}
            if len(eligible_battles[0]["players"]) == 1:
                new_player["plrX"] = 3150
                new_player["plrY"] = 1200
                new_player["angle"] = 90
                new_player["maxhp"] = maxhp
                new_player["hp"] = maxhp
            eligible_battles[0]["players"].append(new_player)
        else:
            # If there are no eligible battles, create a new one and add the player
            new_player = {"plrID": ID, "plrX": 3125, "plrY": 9500,"angle":270,"BID": BID,"SID":SID,"maxhp":maxhp,"hp":maxhp,"stars":0,"charge":3000}
            new_battle = {
                "id": len(self.battles) + 1,
                "GameObjeckCount": 0,
                "LogicItem": [],
                "killlist": [],
                "battleTick": 0,
                "battleStart": False,
                "players": [new_player]
            }
            self.battles.append(new_battle)
    def get_battle_for_id(self, id):
        for battle in self.battles:
            if battle["id"] == id:
                return battle
        return None
    def Leave_Battle(self,battleID, id):
        for player in self.battles[battleID-1]["players"]:
            if player["plrID"] == id:
                self.battles[battleID-1]["players"].remove(player)
                return True
        return False
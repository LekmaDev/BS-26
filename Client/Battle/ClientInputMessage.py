from Server.Battle.VisionUpdate import VisionUpdate
from Utils.Reader import BSMessageReader
from Utils.BitStream import BitStream
from Utils.MatchmakingLogic import MatchmakingLogic
import math
import random
from Files.CsvLogic.Cards import Cards
from Logic.Battle.Objects.LogicProjectileServer import LogicProjectileServer
class ClientInputMessage(BitStream):
	def __init__(self, client, player, initial_bytes):
		super().__init__(initial_bytes)
		self.player = player
		self.client = client
		self.matchmaker = MatchmakingLogic()
		self.my_battle = self.matchmaker.get_battle_for_id(self.player.battleID)
		self.index = 0
		self.type = 2
		self.x = 0
		self.y = 0
		self.sender_id = None
		
	def decode(self):
		self.readPositiveInt(14)
		self.readPositiveInt(10)
		self.readPositiveInt(13)
		self.readPositiveInt(10)
		
		count = self.readPositiveInt(5)
		for i in range(count):
			self.index = self.readPositiveInt(15)
			self.player.dudu = self.index
			if self.my_battle["players"][0]["plrID"] == self.player.low_id:
				self.sender_id = 0
			elif self.my_battle["players"][1]["plrID"] == self.player.low_id:
				self.sender_id = 1
			else:
				self.sender_id = None
			
			self.type = self.readPositiveInt(4)
			
			if self.sender_id is not None and self.type == 2:
				player = self.my_battle["players"][self.sender_id]
				x1, y1 = self.readInt(15), self.readInt(15)
				x2, y2 = player["plrX"], player["plrY"]
				speed = 0.3
				delta_x, delta_y = x1 - x2, y1 - y2
				player["plrX"] = x2 + (speed * delta_x)//1
				player["plrY"] = y2 + (speed * delta_y)//1
				angle_in_degrees = math.degrees(math.atan2(y1 - y2, x1 - x2))
				angle_in_degrees += 360 * (angle_in_degrees < 0)
				player["angle"] = angle_in_degrees
			if self.sender_id is not None and self.type == 0:
				player = self.my_battle["players"][self.sender_id]
				if player["charge"] > 0:
					player["charge"] -= 1000
					x1, y1 = self.readInt(15), self.readInt(15)
					x2, y2 = player["plrX"]+x1+x1,player["plrY"]+y1+y1
					angle = math.degrees(math.atan2(y2-player["plrY"], x2-player["plrX"]))
					if angle < 0:angle += 360
					id = LogicProjectileServer.getItem(player["BID"],self)
					if id == 12 or id == 8:
						for i in range(2):
							my_array = [{"x":player["plrX"],"y":player["plrY"],"ToX":x1,"ToY":y1,"angle":angle//1,"id":id,"Tick":0,"sender":self.player.low_id}]
							self.my_battle["LogicItem"].append(my_array)
					else:
						my_array = [{"x":player["plrX"],"y":player["plrY"],"ToX":x1,"ToY":y1,"angle":angle//1,"id":id,"Tick":0,"sender":self.player.low_id}]
						self.my_battle["LogicItem"].append(my_array)
	def process(self):
		VisionUpdate(self.client, self.player, self.my_battle).send()
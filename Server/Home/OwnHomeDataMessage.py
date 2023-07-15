from Utils.Writer import Writer
from database.DataBase import DataBase
from Logic.Shop import Shop
import json
from datetime import datetime
from Server.Club.AllianceDataMessage import AllianceDataMessage
class OwnHomeDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player
        self.timestamp = int(datetime.timestamp(datetime.now()))

    def encode(self):
        DataBase.loadAccount(self)

        self.writeVint(self.timestamp)
        self.writeVint(self.timestamp)  # Timestamp

        self.writeVint(self.player.trophies)  # Player Trophies
        self.writeVint(self.player.highest_trophies)  # Player Max Reached Trophies
        self.writeVint(self.player.highest_trophies)
        self.writeVint(self.player.Troproad)  #self.player.Troproad
        self.writeVint(220+self.player.player_experience)  # Player exp
        #DataBase.replaceValue(self, "Troproad", 1)
        self.writeScId(28, self.player.profile_icon)  # Player Icon ID
        self.writeScId(43, self.player.name_color)  # Player Name Color ID

        self.writeVint(0)  # array

        # Selected Skins array
        self.writeVint(1)
        self.writeVint(29)
        self.writeVint(self.player.skin_id)  # skinID

        # Unlocked Skins array
        self.writeVint(len(self.player.UnlockedSkins))
        for i in self.player.UnlockedSkins:
            if self.player.UnlockedSkins[str(i)]==1:
                self.writeScId(29, int(i))
            else:
                self.writeScId(29, 0)

        self.writeVint(0)  # array

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeBoolean(False)  # "token limit reached message" if true
        self.writeVint(1)
        self.writeBoolean(True)

        self.writeVint(0)  # Token doubler ammount
        self.writeVint(172800)  # Season End Timer
        self.writeVint(172800)
        self.writeVint(172800)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)  # array

        self.writeByte(8)  # related to shop token doubler

        self.writeBoolean(True)
        self.writeBoolean(True)
        self.writeBoolean(True)

        self.writeVint(0)
        self.writeVint(0)

        # Shop Array
        Shop.EncodeShopOffers(self)
        # Shop Array End


        self.writeVint(0)  # array

        self.writeVint(0)
        self.writeVint(0)  # Time till Bonus Tokens (seconds)

        self.writeVint(0)  # array

        self.writeVint(self.player.tickets)  # Tickets
        self.writeVint(0)

        self.writeScId(16, self.player.brawler_id)  # Selected Brawler

        self.writeString("BY")  # Location
        self.writeString(f"{self.player.ccc}")  # Supported Content Creator

		# Animation ID
        if self.player.bet != 0:
            self.writeVint(1) # Count
            self.writeInt(4)
            if self.player.bet < 0:
                self.writeInt(0)#+ тррофей анимка кр
            else:
                self.writeInt(self.player.bet)#+ тррофей анимка кр
        else:
            self.writeVint(0)  # array
        self.writeVint(0)  # array
        self.writeVint(0)  # array
        self.writeVint(0)  # array

        self.writeBoolean(False)

        self.writeVint(2019049)

        self.writeVint(100)
        self.writeVint(10)

        self.writeVint(30)
        self.writeVint(3)
        self.writeVint(80)
        self.writeVint(10)
			
        self.writeVint(50)
        self.writeVint(1000)

        self.writeVint(500)
        self.writeVint(50)
        self.writeVint(999900)

        self.writeVint(0)  # array

        self.writeVint(8)  # array

        self.writeVint(1)
        self.writeVint(2)
        self.writeVint(3)
        self.writeVint(4)
        self.writeVint(5)
        self.writeVint(6)
        self.writeVint(7)
        self.writeVint(8)
		

        # Logic Events
        self.writeVint(2)
 
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(0)  # IsActive | 0 = Active, 1 = Disabled
        self.writeVint(86400)  # Timer

        self.writeVint(0)
        self.writeScId(15, 24)

        self.writeVint(3)

        self.writeString()
        self.writeVint(0)
        self.writeVint(0)  # Powerplay game played
        self.writeVint(0)  # Powerplay game left maximum

        self.writeBoolean(False)

        self.writeVint(0)
        self.writeVint(0)
        
        
        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(0)  # IsActive | 0 = Active, 1 = Disabled
        self.writeVint(86400)  # Timer

        self.writeVint(0)
        self.writeScId(15, 32)

        self.writeVint(3)

        self.writeString()
        self.writeVint(0)
        self.writeVint(0)  # Powerplay game played
        self.writeVint(0)  # Powerplay game left maximum

        self.writeBoolean(False)

        self.writeVint(0)
        self.writeVint(0)   

        self.writeVint(0)  # array

        # Logic Shop

        self.writeVint(8)
        self.writeVint(20)
        self.writeVint(35)
        self.writeVint(75)
        self.writeVint(140)
        self.writeVint(290)
        self.writeVint(480)
        self.writeVint(800)
        self.writeVint(1250)

        self.writeVint(8)
        self.writeVint(1)
        self.writeVint(2)
        self.writeVint(3)
        self.writeVint(4)
        self.writeVint(5)
        self.writeVint(10)
        self.writeVint(15)
        self.writeVint(20)

        self.writeVint(3)
        self.writeVint(10)
        self.writeVint(30)
        self.writeVint(80)

        self.writeVint(3)
        self.writeVint(6)
        self.writeVint(20)
        self.writeVint(60)

        self.writeVint(1)#GOLD PACK #1
        self.writeVint(10)#GOLD PACK cOST #1

        self.writeVint(1)#GOLD PACK #1
        self.writeVint(1337)#GOLD PACK aMMO #1

        self.writeVint(2)  # array
        self.writeVint(200)  # Max Tokens
        self.writeVint(20)  # Plus Tokens

        self.writeVint(8640)
        self.writeVint(10)
        self.writeVint(5)

        self.writeVint(6)

        self.writeVint(50)
        self.writeVint(604800)

        self.writeBoolean(True)  # Box boolean

        self.writeVint(0)  # array

        self.writeVint(1)  # Menu Theme
        self.writeInt(1)
        self.writeInt(41000000 + self.player.theme)  # Theme ID

        self.writeVint(0)  # array

        self.writeInt(0)
        self.writeInt(1)

        self.writeVint(1)  # array
        # Custom Support Message Notification
        self.writeVint(81) # Notification ID
        self.writeInt(1) # Notification Index
        self.writeBoolean(False) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString(f"Добро пожаловать в <c8bfd28>V<c68fb51>B<c45f97a>C<c22f7a3> <c09f5cc>B<c00f5cc>R<c19f7a3>A<c33f97a>W<c4cfb51>L</c>!\nТвой ID: <c57fa66>{self.player.low_id}</c>\nКупить привилегию VIP TG - <c60fa5a>v<c4df971>b<c39f888>c<c26f79e>s<c13f6b5>u<c00f5cc>p<c00f5cc>p<c0ef6b5>o<c1cf79e>r<c2af887>t<c38f971>_<c47fa5a>b<c55fb43>o<c63fc2d>t</c>\nНовостной <c82fc33>T<c57fa66>e<c2bf799>l<c00f5cc>e<c20f799>g<c40fa66>r<c60fc33>a<c80ff00>m</c> канал: t.me/vbcbrawl\n") # Notification Message Entry       
        self.writeVint(0)
        # Custom Support Message Notification End
		

        self.writeVint(1)

        self.writeBoolean(True)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)  # High Id
        self.writeVint(self.player.low_id)  # Low Id

        self.writeVint(0)
        self.writeVint(self.player.low_id)

        self.writeVint(0)
        self.writeVint(self.player.low_id)
		
        if self.player.name == "VBC26":
            self.writeString("VBC26")  # Player Name
            self.writeVint(0)
        else:
            self.writeString(f"{self.player.name}")  # Player Name
            self.writeVint(1)

        self.writeInt(0)

        self.writeVint(8)

        # Unlocked Brawlers & Resources array
        self.writeVint(len(self.player.card_unlock_id) + 4)  # count

        index = 0
        for unlock_id in self.player.card_unlock_id:
            self.writeScId(23, unlock_id)
            try:
                self.writeVint(self.player.UnlockedBrawlers[str(index)])
            except:
                self.writeVint(1)
            index += 1

        self.writeVint(5)  # csv id
        self.writeVint(1)  # resource id
        self.writeVint(self.player.box)  # resource amount

        self.writeVint(5)  # csv id
        self.writeVint(8)  # resource id
        self.writeVint(self.player.gold)  # resource amount

        self.writeVint(5)  # csv id
        self.writeVint(9)  # resource id
        self.writeVint(self.player.bigbox)  # resource amount

        self.writeVint(5)  # csv id
        self.writeVint(10)  # resource id
        self.writeVint(self.player.starpoints)  # resource amount

        # Brawlers Trophies array
        self.writeVint(len(self.player.brawlers_trophies))  # brawlers count
        for brawler_id, trophies in self.player.brawlers_trophies.items():
                self.writeScId(16, int(brawler_id))
                self.writeVint(self.player.brawlers_trophies[f"{int(brawler_id)}"])


        # Brawlers Trophies for Rank array
        self.writeVint(len(self.player.brawlers_trophies))  # brawlers count
        for brawler_id, trophies in self.player.brawlers_trophies.items():
                self.writeScId(16, int(brawler_id))
                self.writeVint(self.player.brawlers_trophies[f"{int(brawler_id)}"])

        self.writeVint(0)  # array

        # Brawlers Upgrade Points array
        self.writeVint(len(self.player.brawlerPoints))  # brawlers count
        for brawler_id, trophies in self.player.brawlerPoints.items():
                self.writeScId(16, int(brawler_id))
                self.writeVint(self.player.brawlerPoints[f"{int(brawler_id)}"])

        # Brawlers Power Level array
        self.writeVint(len(self.player.brawlerPowerLevel))  # brawlers count
        for brawler_id, trophies in self.player.brawlerPowerLevel.items():
                self.writeScId(16, int(brawler_id))
                self.writeVint(self.player.brawlerPowerLevel[f"{int(brawler_id)}"])
        # Gadgets and Star Powers array
        self.writeVint(1)  # count
 
        self.writeVint(23)
        self.writeVint(3)
        self.writeVint(1)

        # "new" Brawler Tag array
        self.writeVint(0)  # brawlers count
        
        self.writeVint(self.player.gems)  # Player Gems
        self.writeVint(self.player.gems)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(2)
        self.writeVint(1585502369) 
        DataBase.replaceValue(self, 'online', 2)
        if self.player.gold < 0:
            self.player.gold = 0
            DataBase.replaceValue(self, 'gold', self.player.gold)
        if self.player.gems < 0:
            self.player.gems = 0
            DataBase.replaceValue(self, 'gems', self.player.gems)
        if self.player.vip == 0:
            config = open('config.json', 'r')
            content = config.read()
            settings = json.loads(content)
            if self.player.low_id in settings['vips']:
                DataBase.replaceValue(self, 'vip', 1)
        if self.player.club_low_id > 0:
            AllianceDataMessage(self.client, self.player, 0, self.player.club_low_id).send()
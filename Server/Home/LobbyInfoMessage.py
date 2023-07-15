from Utils.Writer import Writer
from datetime import datetime
class LobbyInfoMessage(Writer):
    def __init__(self, client, player, count):
        super().__init__(client)
        self.id = 23457
        self.player = player
        self.count = count

    def encode(self):
        now = datetime.now()
        self.writeVint(0)
        self.writeString()
        self.writeVint(0)
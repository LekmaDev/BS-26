class LogicCharacterServer:
    def encode(stream,my_battle,self):
        self.my_battle = my_battle
        x1, y1 = self.x, self.y
        x2, y2 = player["plrX"], player["plrY"]
        speed = 0.4
        delta_x, delta_y = x1 - x2, y1 - y2
        player["plrX"] = x2 + (speed * delta_x)//3
        player["plrY"] = y2 + (speed * delta_y)//3
        angle_in_degrees = math.ceil(math.degrees(math.atan2(self.y - player["plrY"], self.x - player["plrX"])))
        if angle_in_degrees < 0:
            angle_in_degrees += 360
        player["angle"] = angle_in_degrees
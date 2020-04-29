class AgentEnv:
    def __init__(self,name,posx,posy,orientation):
        self.name = name
        self.posx = posx
        self.posy = posy
        self.orientation = orientation

    def UpdatePosition(self,action):
        if action == "FORWARD":
            if self.orientation == 0:
                self.posx -= 1
            elif self.orientation == 90:
                self.posy += 1
            elif self.orientation == 180:
                self.posx += 1
            elif self.orientation == 270:
                self.posy -= 1

        elif action == "RIGHT":
            self.orientation = (self.orientation+90)%360

        elif action == "LEFT":
            self.orientation = (self.orientation-90)%360
            

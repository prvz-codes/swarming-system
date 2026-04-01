from Entities.Mission import Mission
# from Entities.Position import Position
class Drones(Mission):
    def __init__(self, name : str , id : int):
        self.x = 0
        self.y = 0
        Mission.__init__(self , 0)
        self.name = name
        self.id=id
        self.isLeader=False
        self.battery :int = 100
    # @property
    # def Battery(self):
    #     return self.battery
    # @property
    # def DroneId(self):
    #     return self.id
    # @property
    # def DroneName(self):
    #     return self.name
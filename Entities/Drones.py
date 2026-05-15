from Entities.Mission import Mission
from .Coordinates import Coordinates
# from Entities.Position import Position
class Drones(Mission):
    def __init__(self,id : int  ,  status :str , name : str  ):
        self.x = 0.0
        self.y = 0.0
        self.name = name
        self.id=id
        self.isLeader=False
        self.battery :int = 100
        self.status = status
    # @property
    # def Battery(self):
    #     return self.battery
    # @property
    # def DroneId(self):
    #     return self.id
    # @property
    # def DroneName(self):
    #     return self.name
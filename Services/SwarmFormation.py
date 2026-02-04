from Entities.Drone import Drone
class SwarmFormation():
    
    def __init__(self , gap : int):
        self.__leader = None
        self.gap=gap

    def assignLeader(self , drone:Drone):
        self.__leader = drone
    
    def formation(self ,drones : list [Drone] , noOfDrones : int):
        pass



        
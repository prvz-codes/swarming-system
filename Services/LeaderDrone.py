from Entities.Drone import Drone
class LeaderDrone:
    def __init__(self) -> None:
        self.lead : Drone 
        self.workerDrones :int
        

    # def assignLeader(self , drones : list[Drone]):
    def chooseLeader(self ,  drones : list[Drone] , leaderIdx : int   ):
        self.lead   = drones.pop(leaderIdx)

        self.workerDrones = len(drones)
        self.lead.posX = self.lead.posY = 0
        self.lead.isLeader = True
    @property
    def show(self):
        print(self.lead.name,"is Swarm's leader drone , co-ordinates (" , self.lead.posX , " , " ,self.lead.posY,")")
    @property
    def myLead(self):
        return self.lead
    @property
    def myWorkerDrones(self):
        return self.workerDrones
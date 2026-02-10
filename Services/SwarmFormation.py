from Entities.Drone import Drone
from Services.LeaderDrone import LeaderDrone
# from Services.BatteryTracking import BatteryTracking
class SwarmFormation():
    
    def __init__(self , gap : int):
        self.__leader = None
        self.gap=gap
        

    
    def formation(self ,drones : list [Drone] ,   leaderIdx : int ,  formationName : str , leadDrone : LeaderDrone ):
        
        leadDrone.chooseLeader(drones , leaderIdx)
        # lead = leadDrone.lead

        noOfWorkerDrones = leadDrone.myWorkerDrones


        half  = noOfWorkerDrones % 2
        posVal  = 0
        
       
        for i in range (0 , noOfWorkerDrones):
            drones[i].taskStatus = "assigned "

        if(formationName is "Line" or  "Column"):
            for i in range(0 , half):
                if(formationName is "Line"):
                    # trackTask.tracking(drones[i])
                    drones[i].degreeY = posVal - 1
                    # trackBattery.updateBattery(drones[i])
                    
                elif(formationName is "Column"):
                    drones[i].degreeX = posVal - 1
                    # trackTask.tracking(drones[i])
                    # trackBattery.updateBattery(drones[i])

                    


            for i in range(half , noOfWorkerDrones):

                # drones[half].isTaskAssigned = True
                if(formationName is "Line"):
                    drones[half].degreeX = i+1
                    # trackTask.tracking(drones[i])
                    # trackBattery.updateBattery(drones[i])
                elif(formationName is "Column"):
                    drones[half].degreeX = i+1
                    # trackTask.tracking(drones[i])
                    # trackBattery.updateBattery(drones[i])
                # drones[i].taskStatus = "completed"
        if(formationName is "Square" or  "Rectangle" or "Grid"):
            pass
        if(formationName is "Diamond"):
            pass
            
                    
from Entities.Drone import Drone
from Entities.Status import Status
from Services.SwarmFormation import SwarmFormation
from Services.BatteryTracking import BatteryTracking
from Services.FailedDrone import FailedDrone
from Services.LeaderDrone import LeaderDrone
from Services.StatusUpdation import StatusUpdation


class SystemHandler():
    def __init__(self , swarm : SwarmFormation , battery : BatteryTracking ,fail : FailedDrone , leadDrone : LeaderDrone  , status : Status):
        self.swarm = swarm
        self.battery = battery
        self.fail = fail
        self.status = status
        self.leadDrone = leadDrone
  
    def operation(self ,   drones  : list[Drone]):
        
        for i in range(len(drones) -1, -1 , -1):
            
            if(self.battery.
               checkBattery(drones[i])):
                self.fail.failed(drones[i])
                StatusUpdation.setStatus(drones[i] , "failed")
                print("failed drones name :"  , drones[i].name , " battery : " , drones[i].battery )
                drones.pop(i)
            # print("drone " , i ," location cordinates : ( " , drones[i].posX , " , " , drones[i].posY , " )")
           
            else:
                StatusUpdation.setStatus(drones[i] , "active")
        
        
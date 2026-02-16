from Entities.Position import Position
from Entities.Degree import Degree
from Entities.Mission import Mission
from Entities.Status import Status
from Entities.Swarm import Swarm
from Entities.Drone import Drone
from Services.SwarmFormation import SwarmFormation
from Services.BatteryTracking import BatteryTracking
from Services.FailedDrone import FailedDrone
from Services.LeaderDrone import LeaderDrone
from Services.StatusUpdation import StatusUpdation
from Services.system_handler_service import SystemHandler

def main():
    
    print("Swarm system initialized")
    myDrones = [
    Drone(1, "DJI Phantom"),
    Drone(2, "DJI Mavic"),
    Drone(3, "Parrot Anafi"),
    Drone(4, "Autel Evo"),
    Drone(5, "Skydio 2"),
    Drone(6, "Holy Stone HS720"),
    Drone(7, "Potensic D85"),
    Drone(8, "Hubsan Zino")
]
    swarm = SwarmFormation(gap=5)
    myBattery = BatteryTracking()
    failed = FailedDrone()
    lead = LeaderDrone()
    # myDrones[0].battery =  0
    # myDrones[2].battery =  2
    # myDrones[5].battery =  5
    # myDrones[1].battery =  1
    # # myDrones[3].battery =  3
    # # myDrones[4].battery =  4
    # myDrones[6].battery =  6
    # myDrones[7].battery =  7

    status = Status()
    
    tasks  = [ "Column" ,"Line"]

    operateSwarm  =  SystemHandler(swarm , myBattery , failed  , lead , status)
    # for i in range(0 , len(myDrones)):
    #     print(myDrones[i].battery)

    
    operateSwarm.operation(myDrones , tasks)


if __name__ == "__main__":
    main()

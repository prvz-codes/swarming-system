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

    while True:
        print("\n===== SWARM DRONE CONTROL SYSTEM =====")
        print("1. Add Drone")
        print("2. View All Drones")
        print("3. Assign Task to All Drones")
        print("4.enter an operation  (move ,attack/drop ,land, takeoff , takepic)")
        print("5.enter a formation (line , column)")
        
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter drone name: ")
            id = int(input("Enter battery level: "))
            drone = Drone(id , name)
            myDrones.append(drone)
            print("Drone added successfully.")

        elif choice == "2":
            for d in myDrones:
                print("Name:", d.name, "| id:", d.id)

        elif choice == "3":
            task = input("Enter task name: ")
            tasks.append(task)
            print("Task added.")

        elif choice == "4":
            msg = input("(move ,attack/drop ,land, takeoff , takepic)")
            # if msg.lower() == "move" or "drop" or "takepic":
            xAxis= int(input("X-coordinate :"))
            yAxis= int(input("Y-coordinate :"))
            operateSwarm.operation(myDrones )
            operateSwarm.swarm.perform(myDrones , 1 , operateSwarm.leadDrone , msg ,xAxis    ,yAxis)
        elif choice == "5":
            
            operateSwarm.operation(myDrones)
            operateSwarm.swarm.formation(myDrones , 1 , tasks , operateSwarm.leadDrone)
        
        elif choice == "7":
            print("Exiting system...")
            break

        else:
            print("Invalid choice.")
        
        


if __name__ == "__main__":

    main()

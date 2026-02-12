from Entities.Drone import Drone
# from Services.system_handler_service import SystemHandler



class BatteryTracking:
    def __init__(self):
        pass

    def updateBattery(self , drone : Drone):
        drone.battery = drone.battery -  10

    
    def checkBattery(self , drone : Drone ):
        if(drone.battery < 10):
            return True
        else:
            return False
            # return a signal

           
            

  
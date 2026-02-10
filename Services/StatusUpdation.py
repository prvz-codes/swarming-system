from Entities.Drone import Drone

class StatusUpdation:

    def __init__(self) -> None:

        pass
    @staticmethod
    def setStatus( drone : Drone , msg :str ):
        
        drone.failed = False
        drone.active = False
        drone.idle = False
        if(msg == "failed"):
            drone.failed = True
        if(msg == "active"):
            drone.active = True
        if(msg == "idle"):
            drone.idle = True

            return drone
            
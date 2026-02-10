# from Services.SwarmFormation import SwarmFormation
# from Entities.Mission import Mission
from Entities.Drone import Drone

class ProgressTracking():
    def __init__(self ):
        self.__progress : int

    # def setProgress(self, progress : int):
    #     self.__progress+=progress

    def tracking(self , drone : Drone):
        if(drone.isTaskAssigned == True and drone.taskStatus is "executing"):
            self.__progress += 10
    
    @property
    def retrieveProgress(self):
        return self.__progress    
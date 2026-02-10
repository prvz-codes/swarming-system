from Entities.Drone import Drone
# from Entities.Controller import Controller

class FailedDrone:
    def __init__(self , ) -> None:
       pass 

    def failed(self ,drone : Drone):
        drone.isTaskAssigned = False
        drone.degreeX = drone.degreeY= -100

        drone.isLeader = False
        drone.taskStatus = "none"
        
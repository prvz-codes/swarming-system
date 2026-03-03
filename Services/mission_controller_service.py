# from Entities.Mission import Mission

from data_layer.db_context import DbContext
import time
class MissionController:
    def __init__(self  , db : DbContext):
        self.db = db
    
    
    def performMissions(self , x : int , y : int , missionName :str):
            if(missionName.lower() == "move"):
                self.move(x , y)
            elif(missionName.lower() == "landing"):
                self.landing()
            elif(missionName.lower() == "takeoff"):
                self.takeoff(y)
            elif(missionName.lower() == "swarmaround"):
                self.swarmAround(x, y)
            elif(missionName.lower() == "show"):
                self.showPos()
            else:
                 print("Invalid operation!!! :")
            # choose leader
            # check type of mission
            
        
    def formationMission(self  ):
        pass
    def move(self , x :int , y : int , ):
        for i in range(0 , len(self.db.dronesList)):
             self.db.dronesList[i].x=x
             self.db.dronesList[i].y=y
        
    def landing(self):
        for i in range(0 , len(self.db.dronesList)):
             self.db.dronesList[i].x=0
             self.db.dronesList[i].y=0
    def takeoff(self , y : int):
        for i in range(0 , len(self.db.dronesList)):
             self.db.dronesList[i].y+=y
    def showPos(self):
        for i in range(0 , len(self.db.dronesList)):
            print(" DRONE {self.db.droneList[i].name}  is AT NOW POS :" ,   self.db.dronesList[i].x ,   self.db.dronesList[i].y)
    def swarmAround(self ,  x:int  , y : int):
        

        for i in range(1 , 5):

            match i:
                case  1:
                    self.move(x , y+1)
                   
                case 2:
                    self.move(x-1 , y)
                    
                case 3:
                    self.move(x+1,y)    
                    
                case 4:
                    self.move(x , y-1)
                case _: pass
            print(" DRONES  ARE SWARMING AT POS :" ,   self.db.dronesList[i].x ,   self.db.dronesList[i].y)
            time.sleep(1)
         
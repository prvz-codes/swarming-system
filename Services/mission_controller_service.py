# from Entities.Mission import Mission
# import json
import httpx
import asyncio
from data_layer.db_context import DbContext
from Entities.Drones import Drones
from Services.log_service import LogService
from Entities.Coordinates import Coordinates
from Services.Requests import Requests

class MissionController:
    def __init__(self  , db : DbContext , missionLog : LogService , radarRangeCoordinates  : Coordinates ,  requests : Requests , dronesList : list[Drones]):
        self.db = db
        self.missionLog = missionLog
        self.dronesList = dronesList
        self.requests = requests
        self.radarRangeCoordinates = radarRangeCoordinates
    
    
    # def performMissions(self , x : int , y : int , taskName :str):
            
    #         if(taskName.lower() == "move"):
    #             self.move(x , y)
    #         elif(taskName.lower() == "landing"):
    #             self.landing()
    #         elif(taskName.lower() == "takeoff"):
    #             self.takeoff(y)
    #         elif(taskName.lower() == "swarmaround"):
    #             self.swarmAround(x, y)
    #         elif(taskName.lower() == "show"):
    #             self.showPos()
    #         else:
    #              print("Invalid operation!!! :")
    #         # choose leader
    #         # check type of mission
            
        
    def formationMission(self  ):
        pass
    def move(self , taskName :str  , coordinates : Coordinates  , taskId : int):
        

        if coordinates.x > coordinates.y :
            length = coordinates.y 
        else:
            length = coordinates.x
        
        for h in range(0 ,int(length)):
            tracker :int=  0
            
            while(tracker < len(self.dronesList)):
                if(self.dronesList[tracker].x < coordinates.x):
                    
                    self.dronesList[tracker].x+=1
                    self.missionLog.CoordinatesLogTask(taskName , taskId , coordinates)                    
                if(self.dronesList[tracker].y < coordinates.y):
                    self.dronesList[tracker].y+=1
                    self.missionLog.CoordinatesLogTask(taskName , taskId , coordinates)
                print(self.dronesList[tracker].name , " X : " ,  self.dronesList[tracker].x , " Y : " ,  self.dronesList[tracker].y)
                tracker +=1

    async def landing(self ,  taskName :str   , taskId : int):
        print("landing...")
        for drone in self.dronesList:
            allLanded =  True
            if drone.x!=0 or drone.y!= 0 :
                allLanded = False
                code = await self.requests.requestRunway(drone.id)
                if code == 200 :
                    drone.x = 0
                    drone.y = 0
                    self.db.logDb.insert_one({"taskId" : taskId ,"taskName" :   taskName , "droneid" : drone.id ,"message" : "drone landed successfully" })
                elif code == 502 :
                    self.db.logDb.insert_one({"taskId" : taskId ,"taskName" :   taskName , "droneid" : drone.id ,"message" : "landing permission denied" })
            if allLanded :
                break
            
            await asyncio.sleep(2)

                    
        
    def takeoff(self , taskName :str   , taskId : int):
        print("taking off...")
        
        for i in range(0 , len(self.dronesList)):
             self.dronesList[i].y+=1
        self.db.logDb.insert_one({"taskId" : taskId ,"taskName" : taskName })
    def action(self , act  :str , taskName :str   , taskId : int ):
        if(act == "take_photo"):
            print("tasking picture")
           
            self.db.logDb.insert_one({"taskId" : taskId ,"taskName" : taskName, "Action" : act })
            
             
    def showPos(self):
        for i in range(0 , len(self.dronesList)):
            print( self.dronesList[i].name  , " is AT NOW POS :" ,   self.dronesList[i].x ,   self.dronesList[i].y)
    # def swarmAround(self ,  x:int  , y : int):
        
    #     for i in range(1 , 5):

    #         match i:
    #             case  1:
    #                 self.move(x , y+1)
                   
    #             case 2:
    #                 self.move(x-1 , y)
                    
    #             case 3:
    #                 self.move(x+1,y)        
                    
    #             case 4:
    #                 self.move(x , y-1)
    #             case _: pass
    #         print(" DRONES  ARE SWARMING AT POS :" ,   self.dronesList[i].x ,   self.dronesList[i].y)
    #         time.sleep(1)
         
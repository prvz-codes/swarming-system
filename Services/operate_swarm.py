from data_layer.db_context import DbContext

from Services.mission_controller_service import MissionController
from Services.Get_DroNE_service import DroneRecieve
from Services.Get_Task_service import TaskRecieve
from Services.Get import TaskStart
from Services.log_service import LogService



from fastapi import HTTPException


class OperateSystem:
    def __init__(self , db : DbContext,   missionControl : MissionController , recieveDrone : DroneRecieve ,recieveTask : TaskRecieve ):
        self.db =  db
        self.missionControl = missionControl
        self.recieveDrone = recieveDrone
        
        self.recieveTask = recieveTask
        


    def startOperation(self):
        try:
          self.recieveTask.retrieveTask()
          try:
                self.recieveDrone.retrieveDroneData
                try :
                      
                      if(True):#self.db.startMission == "start":
                            i = 0
                            j=0
                            while(i < len(self.db.tasksList)):
                              
                              tasks  = self.db.tasksList[i].tasks
                              while j < len(tasks):
                                    if(tasks[j].tasktype == "TAKEOFF"):
                                          
                                          self.missionControl.takeoff(self.db.tasksList[i].missionName , self.db.tasksList[i].missionId)
                                          
                                    if(tasks[j].tasktype == "MOVE" ):
                                          x= tasks[j].coordinates
                                          if x  is None:
                                                raise ValueError("value null " , tasks[j].coordinates)
                                          self.missionControl.move( self.db.tasksList[i].missionName, x, self.db.tasksList[i].missionId)
                                    if(tasks[j].action == "ACTION"):
                                          act = tasks[j].action
                                          if act is None:
                                               raise ValueError("value null " , tasks[j].coordinates)
                                          self.missionControl.action(act , self.db.tasksList[i].missionName,self.db.tasksList[i].missionId)
                                    if(tasks[j].tasktype == "LAND"):
                                          
                                          self.missionControl.landing(self.db.tasksList[i].missionName , self.db.tasksList[i].missionId)

                              
                except:
                      HTTPException(status_code = 404 , detail="No Input for start mission!!!")
                      return
                    
          except:
                HTTPException(status_code=404 , detail= "no drones added for mission")
        except:
                HTTPException(status_code=404 , detail= "no Mission assigned")
          




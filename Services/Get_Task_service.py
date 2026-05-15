from data_layer.db_context import DbContext
from Entities.Mission import Mission
from Entities.Task import Task
import requests
from fastapi import HTTPException


class TaskRecieve:
    def __init__(self , url : str , db : DbContext) -> None:
        self.url = url
        self.db = db
    def retrieveTask(self):
        
        response  =  requests.get(self.url)
        
        if response.status_code == 200 :
            try:
                data = response.json()
            
                taskList : list[Task]=[]
                for d in data:
                    task= d["tasks"]
                    j=0
                    while(j < len(task)):
                        taskList.append(task[j])
                        j = j+1

                     
                    newMission = Mission(d["mission_id"] , d["name"] , d["description"] , taskList)
                    self.db.tasksList.append(newMission)
                    
                    self.db.save()



            except:
                HTTPException(status_code=response.status_code , detail="couldn't get missions ")
                return

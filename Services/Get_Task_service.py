from data_layer.db_context import DbContext
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
                self.db.tasksList.append(data)
            except:
                HTTPException(status_code=response.status_code , detail="couldn't get Tasks")
                return

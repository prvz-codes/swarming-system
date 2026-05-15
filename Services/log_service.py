from data_layer.db_context import DbContext
from Entities.Coordinates import Coordinates
class LogService:
    def __init__(self , db :DbContext ):
        self.db  = db
        pass
    def CoordinatesLogTask(self , name :str , id : int , coordinates : Coordinates):
        
        self.db.logDb.insert_one({"taskId" : id ,"taskName" : name, "x-coordinate" : coordinates.x , "y-coordinate" : coordinates.y })
    def ActionLogTask(self , name :str , id : int , description : str):
        self.db.logDb.insert_one({"taskId" : id ,"taskName" : name, "description " : description})
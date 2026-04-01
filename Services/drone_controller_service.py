from Entities.Drones import Drones
from data_layer.db_context import DbContext
class DroneController:
    def __init__(self  , db : DbContext):
       
        self.db =db 
    
    def addDrones(self , name : str , id :int):
        self.db.dronest.insert_one({"name" : name , 
              "id"  : id,
              "x" : 0,
              "y" : 0,
              "isLeader" :False
        })
        return True
        for i in range( 0 , len(self.db.dronesList)):
                if(id ==self.db.dronesList[i].id):
                    raise Exception("ALREADY EXISTS!!")
                    return False
        self.db.dronesList.append(Drones(name , id))
        self.db.save()
    def assignLeader(self , id : int):
        
            x : bool=False
            for i in range(0 , len(self.db.dronesList)):
              if(self.db.dronesList[i].isLeader ==True):
                   x =  True
                   raise Exception("Leader Already Exist!!!")
                   return
            if(x == False):
                for i in range(0 , len(self.db.dronesList)):
                    if(self.db.dronesList[i].id == id):
                        self.db.dronesList[i].isLeader = True
                        return True
            else:
                raise Exception("Leader Already Exist!!!")
    def returnDrone(self):
         for i in range(0 , len(self.db.dronesList)):
              if(self.db.dronesList[i].battery < 20):
                   pass
from Entities.User import User
from Entities.Drones import Drones
import json
import os

class DbContext:
    
    base_dir = os.path.dirname(__file__)
    
    UserPath = os.path.join(base_dir , "user_data.json")
    DronesPath =os.path.join(base_dir ,"drones_data.json") 

    def __init__(self ):
        self.userList: list[User]=[]
        self.dronesList:list[Drones]=[]
        
        user_data : list[dict[str , str ]]
        drone_data : list[dict[str , str ]]
        if os.path.exists(self.UserPath):
            with open(self.UserPath , 'r') as f :
                try:
                    user_data  = json.load(f)
                except json.JSONDecodeError:
                    user_data = []
            for i in user_data:
                self.userList.append(User(i["name"] , int(i["password"])))
        else:
            user_data = []
        if os.path.exists(self.DronesPath):
            with open(self.DronesPath , 'r') as d:
                try:
                    drone_data = json.load(d)
                except json.JSONDecodeError:
                    drone_data = []
            for i in drone_data:
                self.dronesList.append(Drones(i["name"] , int(i["id"])))  
        else:
            drone_data= []  
    
    def save(self):
        data : list[dict[str , int | str]] = []

        for u in self.userList:
            data.append({"name":u.name , "password":u.password})
        with  open(self.UserPath , 'w') as f:
            json.dump(data , f , indent=4)

        droneData : list[dict[str , int|str]]=[]
        for d in self.dronesList:
            droneData.append({"name" : d.name , "id":d.id})
        # try:
            with  open(self.DronesPath , 'w') as dr:
                json.dump(droneData , dr , indent=4)
        # except : Exception("drone battery is less we cannot add it")
                

        

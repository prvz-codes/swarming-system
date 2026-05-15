from Entities.User import User
from Entities.Drones import Drones
from Entities.Task import Task
from Entities.Mission import Mission
import json
import os
from pymongo import MongoClient
from Entities.NumberedTask import NumberedTask
class DbContext:
    
    base_dir = os.path.dirname(__file__)
    UserPath = os.path.join(base_dir , "user_data.json")
    DronesPath =os.path.join(base_dir ,"drones_data.json") 
    MissionPath = os.path.join(base_dir , "Mission_data.json")

    def __init__(self ):
        self.client  = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["DroneDB"]
        self.dronest= self.db["drone"]
        self.missionest = self.db["mission"]
        self.logDb = self.db["log"]
        self.userList: list[User]=[]
        self.dronesList:list[Drones]=[]
        self.tasksList : list[Mission] = []
        self.startMission : str         
        user_data : list[dict[str , str ]]
        drone_data : list[dict[str , str ]]
        mission_data: list[dict[str , str ]]
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
                self.dronesList.append(Drones(int(i["id"] ), i["status"] , i["name"]))  
        else:
            drone_data= []
        if os.path.exists(self.MissionPath):
            with open(self.MissionPath, 'r') as d:
                try:
                    self.tasksList = json.load(d)
                except json.JSONDecodeError:
                    self.tasksList = []
             
        else:
            self.tasksList = []  
    
    def save(self):

        
        # data : list[dict[str , int | str]] = []

        # for u in self.userList:
            
        #     data.append({"name":u.name , "password":u.password})
        # with  open(self.UserPath , 'w') as f:
        #     json.dump(data , f , indent=4)

        droneData : list[dict[str , int  | str]]=[]
        missionData : list[dict[str , int | str | list[Task | NumberedTask ] ]] = []
        for d in self.dronesList:
            self.db.dronest.insert_one({"name" : d.name , 
              "status" : d.status,
              "id"  : d.id,
            #   "isLeader" :False
        })
            
            
            droneData.append({"name" : d.name , "id":d.id , "status" : d.status})
        for d in self.tasksList:
            missionData.append({"M-name " : d.missionName ,  "M-id" : d.missionId , "description" : d.description , "tasks": d.tasks})
        try:
            with  open(self.DronesPath , 'w') as dr:
            
                json.dump(droneData , dr , indent=4)
            with open(self.MissionPath , 'w') as dr:
                json.dump(missionData ,dr ,indent=4)
        except : Exception("drone battery is less we cannot add it")
                

        

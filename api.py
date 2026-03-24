from data_layer.db_context import DbContext
from fastapi import FastAPI
from Entities.Drones import Drones
from Entities.User import User
from Services.drone_controller_service import DroneController
from Services.mission_controller_service import MissionController
from pydantic import BaseModel
from fastapi import HTTPException
class userModel(BaseModel):
    name : str
    password : int
class droneModel(BaseModel):
    name : str
    id : int
app = FastAPI()
mydb = DbContext()

droneControl = DroneController(mydb)
missionControl = MissionController(mydb)
@app.post("/users")
def addUser(users : userModel):
    newUser = User(users.name , users.password)
    mydb.userList.append(newUser)
    mydb.save()
    return {"message : user added" }

@app.post("/leaderDrone")
def addLeader(drone : droneModel):
    
    for i in range(0 , len(mydb.dronesList)):
        if(mydb.dronesList[i].isLeader):
            raise HTTPException(status_code=404, detail=mydb.dronesList[i].name + " leader already exist")
            return
    leadDrone = Drones(drone.name , drone.id)
    droneControl.assignLeader(leadDrone.id)

@app.post("/drone")
def addDrone(drone : droneModel):
    for i in range(0 , len(mydb.dronesList)):
        if(drone.id == mydb.dronesList[i].id):
            raise HTTPException(status_code=404, detail= drone.name  + " already exist")
            return
    newDrone = Drones(drone.name , drone.id)
    mydb.dronesList.append(newDrone)
    mydb.save()
    return {"message :drone added" }


@app.get("/drones")
def myDrones():
    return mydb.dronesList

@app.post("/tasks")
def addTasks(x : int  ,  y : int  ,  task  : str):
    missionControl.performMissions(x , y , task)

@app.get("/Position")
def getPos():
    return missionControl.showPos()
    
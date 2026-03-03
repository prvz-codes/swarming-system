from data_layer.db_context import DbContext
from fastapi import FastAPI
from Entities.Drones import Drones
from Entities.User import User
from pydantic import BaseModel

class userModel(BaseModel):
    name : str
    password : int
class droneModel(BaseModel):
    name : str
    id : int
app = FastAPI()
mydb = DbContext()

@app.post("/users")
def addUser(users : userModel):
    newUser = User(users.name , users.password)
    mydb.userList.append(newUser)
    mydb.save()
    return {"message : user added" }


@app.post("/drone")
def addDrone(drone : droneModel):
    newDrone = Drones(drone.name , drone.id)
    mydb.dronesList.append(newDrone)
    mydb.save()
    return {"message :drone added" }



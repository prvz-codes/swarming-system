# from fastapi import APIRouter
# from Entities.Drones import Drones
# from fastapi import HTTPException
# from pydantic import BaseModel
# from Core.dependencies import mydb, droneControl
# router = APIRouter()




# class droneModel(BaseModel):
#     name : str
#     id : int
# @router.post("/leaderDrone")
# def addLeader(drone : droneModel):
    

#     for i in range(0 , len(mydb.dronesList)):
#         if(mydb.dronesList[i].isLeader):
#             raise HTTPException(status_code=404, detail=mydb.dronesList[i].name + " leader already exist")
#             return
#     leadDrone = Drones(drone.name , drone.id)
#     droneControl.assignLeader(leadDrone.id)

# @router.post("/drone")
# def addDrone(drone : droneModel):
    
    
#     success = droneControl.addDrones(drone.name , drone.id)
#     if not success:
#             raise HTTPException(status_code=404, detail= drone.name  + "drone not added!")
#     else:
         
#     # for i in range(0 , len(mydb.dronesList)):
#     #     if(drone.id == mydb.dronesList[i].id):
            
#     #         return
#         newDrone = Drones(drone.name , drone.id)
#         mydb.dronesList.append(newDrone)
#         mydb.save()
#         return {"message :drone added" }


# @router.get("/drones")
# def myDrones():
#     return mydb.dronesList


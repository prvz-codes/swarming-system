import requests
# import asyncio
from Entities.Drones import Drones
from data_layer.db_context import DbContext
from fastapi import HTTPException
class DroneRecieve:
    def __init__(self , url : str , db : DbContext) -> None:
        self.url = url
        self.db = db
        
    def retrieveDroneData(self):
        response =  requests.get(self.url)
        
        if response.status_code == 200:
            try:
                data = response.json()
                for d  in data:
                    drone = Drones(d["drone_id"] , d["status"], d["name"])
                    self.db.dronesList.append(drone)
                    self.db.save()
                    
                raise HTTPException(status_code = response.status_code , detail=" recieved Successfully!")
                    
            except:
                raise HTTPException(status_code = response.status_code , detail="Couldn't recieve Data")
        else : 
            raise HTTPException(status_code = response.status_code , detail="Couldn't recieve Data")
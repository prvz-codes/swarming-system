import requests
import asyncio
from Entities.Drones import Drones
from data_layer.db_context import DbContext
from fastapi import HTTPException
class DroneRecieve:
    def __init__(self , url : str , db : DbContext ) -> None:
        self.url = url
        self.db = db
    async def retrieveDroneData(self):
        response =  requests.get(self.url)
        await asyncio.sleep(1)
        if response.status_code == 200:
            try:
                data = response.json()
                for d  in data:
                    drone = Drones(d["id"], d["name"])
                    self.db.dronesList.append(drone)
                    raise HTTPException(status_code = response.status_code , detail=" recieved Successfully!")
                    
            except:
                raise HTTPException(status_code = response.status_code , detail="Couldn't recieve Data")
        else : 
            raise HTTPException(status_code = response.status_code , detail="Couldn't recieve Data")
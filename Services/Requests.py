from Entities.Coordinates import Coordinates
from Entities.Drones import Drones
import httpx
import asyncio
import json
class Requests:
    def __init__(self , coordinates : list[Coordinates]):

        self.coordinates = coordinates

    async def requestRunway(self ,id:int):
            url = ""

            async with httpx.AsyncClient() as client:
                response= await client.post(url  ,params={"id" : id})
                return  response.status_code

    
    async def checkRadar(self ,drones :  Drones):
            
                for c in self.coordinates:
                 if c.x == drones.x and c.y == drones.y:
                    json_data = json.dumps({"title" : "Drone entered in radar","drone id":drones.id})
                    async with httpx.AsyncClient() as client:
                        await client.post("" , content=json_data)   
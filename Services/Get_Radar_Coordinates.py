from data_layer.db_context import DbContext
import requests

class TaskRecieve:
    def __init__(self , url : str , db : DbContext) -> None:
        self.url = url
        self.db = db
    def retrieveTask(self):
        response  =  requests.get(self.url)

        if response.status_code == 200 :
            try:
                data = response.json()
                self.db.radarCoordinates =(data["x"])
                self.db.radarCoordinates =(data["y"])

            except:
                ValueError("no data recieved" , response.text)
                return

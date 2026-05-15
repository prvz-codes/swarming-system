from data_layer.db_context import DbContext
import requests

class TaskStart:
    def __init__(self , url : str , db : DbContext) -> None:
        self.url = url
        self.db = db
    def start(self):
        response  =  requests.get(self.url)

        if response.status_code == 200 :
            try:
                data = response.json()
                self.db.startMission.append(data)
            except:
                ValueError("no data recieved" , response.text)
                return

from data_layer.db_context import DbContext
from Services.authenticater_service import Authenticater
from Services.drone_controller_service import DroneController
from Services.mission_controller_service import MissionController
from Services.Get_DroNE_service import DroneRecieve
from Services.Get_Task_service import TaskRecieve
from UI.cli import CLI

 
def main():
    db = DbContext()
    auth = Authenticater(db)
    droneControl = DroneController(db)
    missionControl = MissionController(db)
    url = "http://127.0.0.1:8000/docs#/default/myDrones_drones_get"
    recieveDrone = DroneRecieve(url , db)
    recieveTask = TaskRecieve(url , db)

    try:
          recieveTask.retrieveTask()
          try:
            #     recieveDrone.retrieveDroneData()
                

          except:
                ValueError("no drones added for mission")
    except:
          print("no task recieved")




    cli = CLI(auth , droneControl , missionControl)
    cli.menu()

            

if __name__ == "__main__":
        main()
from data_layer.db_context import DbContext
# from Services.authenticater_service import Authenticater
from Services.drone_controller_service import DroneController
from Services.mission_controller_service import MissionController
from Services.Get_DroNE_service import DroneRecieve
# from Services.Get_Task_service import TaskRecieve
# from Services.Get import TaskStart
from Services.log_service import LogService
from Entities.Coordinates import Coordinates
from Entities.Drones import Drones
# from UI.cli import CLI
from Services.operate_swarm import OperateSystem

 
def main():
    db = DbContext()
    # auth = Authenticater(db)
    droneControl = DroneController(db)
    droneUrl = "http://example.com"
    # taskUrl = "http://192.168.100.78:8000/missions"
    # startUrl = ""
    recieveDrone = DroneRecieve(droneUrl, db)
    recieveDrone.retrieveDroneData()
    # recieveTask= TaskRecieve(taskUrl , db)
    # recieveTask.retrieveTask()
    # startMission = TaskStart(startUrl , db)
    c = Coordinates(0,0)
    missionLog = LogService(db)
    readyDrones = list[Drones]
    readyDrones  = droneControl.ValidateSwarm(db.dronesList)
    missionControl = MissionController(db , missionLog ,c,readyDrones  )
    operate = OperateSystem(db , missionControl , recieveDrone , recieveTask , startMission , missionLog)
    operate.startOperation()
    

    # cli = CLI(auth , droneControl , missionControl)
    # cli.menu()

            

if __name__ == "__main__":
        main()
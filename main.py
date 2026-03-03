from data_layer.db_context import DbContext
from Services.authenticater_service import Authenticater
from Services.drone_controller_service import DroneController
from Services.mission_controller_service import MissionController
from UI.cli import CLI

 
def main():
    db = DbContext()
    auth = Authenticater(db)
    droneControl = DroneController(db)
    missionControl = MissionController(db)
    
    cli = CLI(auth , droneControl , missionControl)
    cli.menu()

            

if __name__ == "__main__":
        main()
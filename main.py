from data_layer.db_context import DbContext
from Services.authenticater_service import Authenticater
from Services.drone_controller_service import DroneController
from UI.cli import CLI

 
def main():
    db = DbContext()
    auth = Authenticater(db)
    droneControl = DroneController(db)
    
    cli = CLI(auth , droneControl)
    cli.menu()

            

if __name__ == "__main__":
        main()
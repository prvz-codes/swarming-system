from data_layer.db_context import DbContext


from Services.drone_controller_service import DroneController
from Services.mission_controller_service import MissionController


mydb = DbContext()


droneControl = DroneController(mydb)
missionControl = MissionController(mydb)


from Entities.Mission import Mission

from data_layer.db_context import DbContext
class MissionController:
    def __init__(self , mission : list[Mission] , db : DbContext):
        self.mission = mission
        self.db = db
    
    
    def performMissions(self):
            
            
            # choose leader
            # check type of mission

            pass
        
    def formationMission(self  ):
        pass
    def operateMission(self):
        pass
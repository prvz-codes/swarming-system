from Entities.Coordinates import Coordinates
class Task() : 
    def __init__(self , tasktype :  str   , coordinates : Coordinates | None, action : str | None) :
        self.tasktype = tasktype
        self.coordinates= coordinates
        self.action = action
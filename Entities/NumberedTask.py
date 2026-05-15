from Entities.Task import Task
from Entities.Coordinates import Coordinates
class NumberedTask(Task):
    def __init__(self , tasktype : str , x : float , y : float , ) :
        self.coordinates= Coordinates(x , y)
        self.tasktype = tasktype
from Entities.Task import Task
class Mission:
    def __init__(self  ,  id : int , name :str , description : str , tasks : list[Task]):
        self.missionId = id
        self.missionName = name
        self.description = description
        self.tasks  = tasks
    
from Entities.Position import Position
from Entities.Degree import Degree
from Entities.Mission import Mission
from Entities.Status import Status

# from Entities.Status import Status

class Drone (Position , Degree , Mission ,Status ):
    def __init__(self , ID : int  =0  , name : str= ""  ,  ):

        self.__Id = ID
        self.__name = name
        self.__leader = False
        self.__battery = 100
        self.__taskAssigned = False
        self.posX = 0
        self.posY = 0
        self.taskStatus = " "
        
        
    @property 
    def posY(self):
        return self.posY
    
    @posY.setter
    def posY(self ,x :int):
        self.posY = x
        
    @property 
    def posX(self):
        return self.posX
    
    @posX.setter
    def posX(self ,x :int):
        self.posX = x
    @property 
    def isLeader(self):
        return self.__leader
    
    @isLeader.setter
    def isLeader(self ,leader : bool):
        self.__leader= leader
    
    @property
    def isTaskAssigned(self ):
        return self.__taskAssigned 


    @isTaskAssigned.setter
    def isTaskAssigned(self , assign : bool):
        self.__taskAssigned = assign


    @property
    def battery(self):
        return self.__battery
    
    @battery.setter
    def battery(self, value: int):
        self.__battery = value

    @property 
    def missionID(self):
        return self.missionId
    
    @missionID.setter
    def missionID(self ,x :int):
        self.missionId = x
    
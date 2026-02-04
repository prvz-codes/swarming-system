from Entities.Position import Position
from Entities.Degree import Degree

class Drone (Position , Degree):
    def __init__(self , ID : int  =0  , name : str= ""  , ):

        self.__Id = ID
        self.__name = name
        self.__leader = False
        self.__battery = 0
        self.__taskAssigned = False
        self.posX = 0
        self.posY = 0
        
    
    @property 
    def isLeader(self):
        return self.__leader
    
    @isLeader.setter
    def isLeader(self ,leader : bool):
        self.__leader= leader
    
    @property
    def istaskAssigned(self ):
        return self.__taskAssigned 


    @istaskAssigned.setter
    def istaskAssigned(self , assign : bool):
        self.__taskAssigned = assign


    @property
    def battery(self):
        return self.__battery
    
    @battery.setter
    def battery(self, value: int):
        self.__battery = value


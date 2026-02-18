from Entities.User import User
from Entities.Drones import Drones


class DbContext:
    
    UserPath = "data_layer/user_data.txt"
    DronesPath = "data_layer/drones_data.txt"
    def __init__(self ):
        self.userList: list[User]=[]
        self.dronesList:list[Drones]=[]
        with open(self.UserPath , 'r') as f :
            for l in f:
               
               l = l.strip()
               if(l):
                    name ,  password = l.split(",")
                    myUser= User(name , int(password))
                    self.userList.append(myUser) 
        
        with open(self.DronesPath , 'r') as d:
            for l in d:
                l = l.strip()
                if(l):
                    name , id = l.split(",")
                    newDrone = Drones(name , int(id))
                    self.dronesList.append(newDrone)


    
    def save(self):
        with open(self.UserPath , 'w') as file:
            for i in range(0 , len(self.userList)):
                file.write(self.userList[i].name)
                file.write(",")
                file.write(str(self.userList[i].password))
                file.write("\n")

        

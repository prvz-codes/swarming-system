from Entities.Drone import Drone
from Services.LeaderDrone import LeaderDrone
# from Services.StatusUpdation import StatusUpdation
class SwarmFormation():
    
    def __init__(self , gap : int):
        self.__leader = None
        self.gap=gap
        

    def formSide(self , drones : list [Drone]  , half : int , count : int , msg : str):
        if(msg == "upper" or "right"):
            for j in range(half , count):
                    num = (j-half)+1
                    if(msg == "right"):
                        drones[j].posX = num
                    else:
                         drones[j].posY = num
                    print(drones[j].name , "  co-ordinates(" , drones[j].posX," , "  , drones[j].posY,")")
                    drones[j].posX = drones[j].posY = 0
        # elif(msg == "lower" or "left"):
        #     posVal = posYval = 0
        #     for z in range(0 , half):
        #                 if(msg == "left"):
        #                     drones[z].posX = posVal - 1
        #                 else:
        #                      drones[z].posY = posYval - 1
                             
                        
        #                 print(drones[z].name , "  co-ordinates(" , drones[z].posX," , "  , drones[z].posY,")")
        #                 if(msg == "left"):
        #                     posVal = posVal - 1
        #                 else:
        #                      posYval = posYval - 1
        #                 drones[z].posX = drones[z].posY = 0

        else:
             print("enter valid side to form ")
    
    def formation(self ,drones : list [Drone] ,   leaderIdx : int ,  formationName : list[str] , leadDrone : LeaderDrone ):
        
        leadDrone.chooseLeader(drones , leaderIdx)
        # lead = leadDrone.lead

        noOfWorkerDrones : int = leadDrone.myWorkerDrones


        half : int  = noOfWorkerDrones // 2
        posVal  =  posYval  = 0

        print("total no of worker drones:  " , noOfWorkerDrones)
        print("half drones" , half)
        
        leadDrone.show

        for i in range (0 , noOfWorkerDrones):
            drones[i].taskStatus = "assigned "
        for i in range (0 , len(formationName)):
            
            
            if(formationName[i] == "Line" or  "Column"):
                print("swarm is forming " , formationName[i])
                
                if(formationName[i] == "Line"):
                    
                    print("right side drones :")
                    
                    self.formSide(drones , half , noOfWorkerDrones , "right")
                    
                elif(formationName[i] == "Column"):
                    print("upper side drones :")
                    self.formSide(drones , half , noOfWorkerDrones , "upper")
                    
                        
                    
                    
                if(formationName[i] == "Line"):
                    print("left drones :")
                    for z in range(0 , half):
                        drones[z].posX = posVal - 1
                        print(drones[z].name , "  co-ordinates(" , drones[z].posX," , "  , drones[z].posY,")")
                        posVal = posVal - 1
                        drones[z].posX = drones[z].posY = 0
                    
                elif(formationName[i] == "Column"):
                    print("lower drones :")
                    
                    for z in range(0 , half):
                        drones[z].posY = posYval - 1
                        print(drones[z].name , "  co-ordinates(" , drones[z].posX," , "  , drones[z].posY,")")
                        posYval = posYval - 1
                        drones[z].posX = drones[z].posY = 0
                       
                        
                
               
            if(formationName[i] == "Square" or  "Rectangle" or "Grid"):
                pass
            if(formationName[i] == "Diamond"):
                pass
        
                    
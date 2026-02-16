from Entities.Drone import Drone
from Services.LeaderDrone import LeaderDrone
import time
# from Services.StatusUpdation import StatusUpdation
class SwarmFormation():
    
    def __init__(self , gap : int):
        self.leader :Drone
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

        # else:
        #      print("enter valid side to form ")
    # def stateChange()
    def takeOff(self , drones: list[Drone] , workers:int , yAxis:int ):
            for i in range(0 , workers):
                drones[i].state = "taking off..."
                print(drones[i].state)
                time.sleep(1)
                drones[i].posY+=yAxis
                

    def moving(self , drones: list[Drone] , workers:int , xAxis:int , yAxis : int):
        print("moving")
        
        for i in range(0 , workers):
                drones[i].state = "Changing position..."
                if( i == 0):
                    print(drones[i].state)
                time.sleep(1)
                drones[i].posX+=xAxis
                drones[i].posY+=yAxis

    def landing(self , drones: list[Drone] , workers:int ):
        time.sleep(1)
        
        print("Landing")
        for i in range(0 , workers):
                drones[i].state = "Landing..."
                time.sleep(0.3)
                print(".")
                
                drones[i].posX = drones[i].posY = 0
        print("SWARM LANDED")
    def attacking(self ,drones: list[Drone] , workers:int , xAxis:int , yAxis : int , leadDrone : Drone ):
        # time.sleep(1)
        self.leader.state =  "leader In survelence..."
        print(self.leader.state)
        time.sleep(1)
        actualX = self.leader.posX
        actualY= self.leader.posY
        print("enemy point  " ,xAxis , " , " ,yAxis)


        for i in range(1 , 5):
             if(i==1):
                  self.leader.posX = xAxis+1
                  self.leader.posY = yAxis
                  print("survelence pos  :" ,i , " " ,self.leader.posX , " , " , self.leader.posY)
             if(i==2):
                  self.leader.posY = yAxis+1
                  self.leader.posX = xAxis
                  print("survelence pos  :" ,i , " " ,self.leader.posX , " , " , self.leader.posY)
             if(i==3):
                  self.leader.posX = xAxis-1
                  self.leader.posY = yAxis
                  print("survelence pos  :" ,i , " " ,self.leader.posX , " , " , self.leader.posY)
             if(i==4):
                  self.leader.posY = yAxis-1
                  self.leader.posX = xAxis
                  print("survelence pos  :" ,i , " " ,self.leader.posX , " , " , self.leader.posY)
        self.leader.posX = actualX 
        self.leader.posY=actualY

        for i in range(0 , workers):                
                drones[i].state = "attacking..."
                
                print(drones[i].state)
                time.sleep(1)
                drones[i].posX = xAxis
                drones[i].posY = yAxis
        print("attacked target ", xAxis ,yAxis ,"successfully !!!!")
    
    def perform(self , drones: list[Drone] , leaderIdx : int , leadDrone : LeaderDrone , performName : str , xAxis : int , yAxis :int):
            leadDrone.chooseLeader(drones , leaderIdx)
            self.leader = leadDrone.lead
            print(len(drones))
        # noOfWorkerDrones = leadDrone.myWorkerDrones
            # if performName.lower() in ["move" or "takeoff" or "land" or  "drop" or "attack" ]:
            drones.append(  leadDrone.myLead)
           
            if performName.lower() in "takeoff":
                self.takeOff(drones , len(drones) , xAxis )

            if performName.lower() in "move" :
            #    print("hellp")
               self.moving(drones , len(drones)  , xAxis , yAxis)
               for i in range(0 , len(drones)):
                    print("drones co-ordinates", i , " " , drones[i].posX , " " , drones[i].posY)
            if performName.lower() in "land":
                self.landing(drones , len(drones))
            
            if performName.lower() == "drop":
                print("hell")
                self.attacking(drones , len(drones)  , xAxis , yAxis , self.leader)
                pass
            if performName.lower() in "takepic":
                pass
        
        
            
    def formation(self ,drones : list [Drone] ,   leaderIdx : int ,  formationName : list[str] , leadDrone : LeaderDrone ):
        
        leadDrone.chooseLeader(drones , leaderIdx)
        self.leader = leadDrone.lead

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
            
        
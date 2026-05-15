# # from Entities.User import User
# from Services.authenticater_service import Authenticater
# from Services.drone_controller_service import DroneController
# from Services.mission_controller_service import MissionController
# # from Entities.Mission import Mission
# import time
# class CLI:
#     def __init__(self   , auth:Authenticater , droneControl : DroneController , missionControl : MissionController  ):
#         #  self.missionList = missionList
#          self.missionControl = missionControl
#          self.auth = auth
#          self.droneControl = droneControl

#     def menu(self):
#         while True:
                           
#             print("MAIN MENU\n")
#             print("press 1 to signup ")
#             print("press 2 to login ")
#             print("press 3 to exit ")
#             inp = input("enter your choice  ")
#             if inp == "1":
#                 name= input("enter your name ?")
#                 password =int(input("enter your password ?"))
#                 try :
#                     self.auth.signUp(name , password)
#                     print("creating account!!!")
#                     time.sleep(1) 
#                     print("user created successfully ")
#                 except Exception as e:
#                     print("ERROR :", name , e)
#             elif(inp == "2"):
#                 name= input("enter your name ?")
#                 password =int(input("enter your password ?"))
#                 response =  self.auth.login(name , password)
#                 if(response):
#                     while(True):
#                         print("welcome to the main screen!!")
#                         print("press 1 to add Drones ")
#                         print("press 2 to assign operation tasks (move , attack , take Picture , land , takeoff)")
#                         print("press 3 to assign formation tasks (line , column)")
#                         print("press 4 to assign a leader")
#                         print("press x to exit")
#                         inp1 = input("enter your choice ?? ")
#                         if inp1 == "1":
#                             d_name = input("enter drone name : ")
#                             d_id = int(input("enter drone id "))
                            
#                             try :
#                                 self.droneControl.addDrones(d_id , d_status , d_name , d_id)
#                                 print("adding Drone!!!")
#                                 time.sleep(1) 
#                                 print("drone added successfully ")
#                             except Exception as e:
#                                 print("ERROR :", d_name , e)
#                                 time.sleep(1)
#                         if inp1 == "2":
                           
#                             xCordinate = int(input("enter x co-ordinate"))
#                             yCordinate = int(input("enter y co-ordinate"))
#                             taskName = input("enter name of tasks")
#                             self.missionControl.performMissions(xCordinate ,yCordinate,taskName)

#                         if inp1 == "3":
#                             pass
#                         if inp1 == "4":
#                             droneId  =  int(input("enter leader drone id  "))
#                             try :
#                                 self.droneControl.assignLeader(int(droneId))
#                                 print("Drone {id} assigned leader Successfully!!!" )
#                                 time.sleep(1)
                            
#                             except Exception as x:
#                                 print("Error :" , x)
#                                 time.sleep(1)
#                         if inp1 == "x":
#                             inp = 3
#                             break    


#                 else:
#                     print("user doesn't exist , plz sign up")
#             if  inp == "3":
#                 print("exited!!!")
#                 break
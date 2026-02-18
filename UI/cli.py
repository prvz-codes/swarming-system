# from Entities.User import User
from Services.authenticater_service import Authenticater

import time
class CLI:
    def __init__(self   , auth:Authenticater):
      
         
         self.auth = auth

    def menu(self):
        while True:
                           
            print("MAIN MENU\n")
            print("press 1 to signup ")
            print("press 2 to login ")
            print("press 3 to exit ")
            inp = input("enter your choice  ")
            if inp == "1":
                
                name= input("enter your name ?")
                password =int(input("enter your password ?"))
                try :
                    self.auth.signUp(name , password)
                    print("creating account!!!")
                    time.sleep(1) 
                    print("user created successfully ")
                except Exception as e:
                    print("ERROR :", name , e)
            elif(inp == "2"):
                name= input("enter your name ?")
                password =int(input("enter your password ?"))
                response =  self.auth.login(name , password)
                if(response):
                    print("welcome to the main screen!!")
                            
                else:
                    print("user doesn't exist , plz sign up")
            if  inp == "3":
                print("exited!!!")
                break
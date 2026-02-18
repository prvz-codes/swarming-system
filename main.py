from Entities.User import User
from Services.authentication_service import Authentication
from data_layer.db_context import DbContext
import time

def main():
    db = DbContext()


    while True:
        print("MAIN MENU\n")
        print("press 1 to signup ")
        print("press 2 to login ")
        print("press 3 to exit ")
        inp = input("enter your choice  ")
        if inp == "1" or inp == "2":
            name= input("enter your name ?")
            password =int(input("enter your password ?"))
            myUser = User(name , password)
            auth = Authentication()
            
            if(inp == "1"):
                try :
                    auth.signUp(myUser)
                    print("creating account!!!")
                    time.sleep(1) 
                    print("user created successfully , plz login again")
                except Exception as e:
                     print("ERROR :", myUser.name , e)
            elif(inp == "2"):
                response =  auth.login(myUser)
                if(response):
                     print("welcome to the main screen!!")
                else:
                     print("user doesn't exist , plz sign up")
        if  inp == "3":
             print("exited!!!")
             break        

if __name__ == "__main__":
        main()
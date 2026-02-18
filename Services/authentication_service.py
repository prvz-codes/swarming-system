from Entities.User import User
from data_layer.db_context import DbContext

class Authentication(Exception):
    def __init__(self  ):
        self.myDb = DbContext() 
    def checkList(self , user:User , type : str):
        if(len(self.myDb.userList)>0):
            for i in range(0,len(self.myDb.userList)):
                if(type == "login"):
                    if(user.name == self.myDb.userList[i].name and user.password == self.myDb.userList[i].password):
                        return True
                if(type == "signup"):
                    if(user.name == self.myDb.userList[i].name):
                        raise Exception("Username already exists")
                        return False
            if(type == "signup"):
                return True
            return False
        else:
             self.myDb.userList.append(user)
             return True  
    def login(self , user : User):
            res = self.checkList(user , "login")
            if(res):
                 return True
            return False
            # line = d.readline().strip()
            # name , password  = line.split(",")
           
    def signUp(self , user: User):
            res = self.checkList(user , "signup")
            if(res):
                self.myDb.userList.append(user)
                self.myDb.save()
        # with open("data.txt" , "a") as d:
        #     d.write(user.name)
        #     d.write(",")
        #     d.write(str(user.password))
        #     d.write("\n")
        
            
        
        
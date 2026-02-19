from Entities.User import User
from data_layer.db_context import DbContext

class Authenticater(Exception):
    def __init__(self,myDb :DbContext   ):
        self.myDb =  myDb

    
          
    def login(self , name:str , password:int):
            if(len(self.myDb.userList)>0):
                for i in range(0,len(self.myDb.userList)):
                    if(name == self.myDb.userList[i].name and password == self.myDb.userList[i].password):
                        return True
                
            return False
           
    def signUp(self , name:str , password:int):
           
           if(len(self.myDb.userList)>0):
            for i in range(0,len(self.myDb.userList)):
                if(name == self.myDb.userList[i].name ):
                    raise Exception("ALREADY EXISTS!!")
                    return  
           else:
                self.myDb.userList.append(User(name , password))
                self.myDb.save()
            
        
            
        
        
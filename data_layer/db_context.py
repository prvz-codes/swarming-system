from Entities.User import User

class DbContext:
    
    UserPath = "data_layer/data.txt"
    def __init__(self ):
        self.userList: list[User]=[]
        with open(self.UserPath , 'r') as f:
            for l in f:
               l = l.strip()
               if(l):
                    name ,  password = l.split(",")
                    myUser= User(name , int(password))
                    self.userList.append(myUser) 
        

    def save(self):
        with open(self.UserPath , 'w') as file:
            for i in range(0 , len(self.userList)):
                file.write(self.userList[i].name)
                file.write(",")
                file.write(str(self.userList[i].password))
                file.write("\n")

        

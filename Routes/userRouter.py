# from fastapi import APIRouter
# from pydantic import BaseModel
# from Core.dependencies import mydb
# from Entities.User import User


# router = APIRouter()

# from pydantic import BaseModel
# class userModel(BaseModel):
#     name : str
#     password : int




# @router.get("/users")
# def addUser(users : userModel):
#     newUser = User(users.name , users.password)
#     mydb.userList.append(newUser)
#     mydb.save()
#     return {"message : user added" }



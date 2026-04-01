
from fastapi import FastAPI


from Routes.droneRouter import router as DroneRouter

from Routes.taskRouter import router as TaskRouter

from Routes.userRouter import router as UserRouter


app = FastAPI()

app.include_router(DroneRouter)
app.include_router(UserRouter)
app.include_router(TaskRouter)



    
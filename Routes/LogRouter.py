from fastapi import APIRouter

from Core.dependencies import mydb
from Services.log_service import LogService

router = APIRouter()

@router.get("/withinRadarRange")
async def sendData()
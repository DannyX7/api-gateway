from fastapi import APIRouter, Header
from typing import Dict
import httpx

router = APIRouter(prefix="/onboarding")

SPRING_URL = "http://localhost:8001/"

@router.post("/addstep")
async def addstep(data: Dict, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                SPRING_URL + "onboarding/addstep",
                json=data,
                headers={"Token": Token}
            )
            return response.json()
        except Exception as e:
            return {"code": 500, "message": str(e)}

@router.get("/getallsteps")
async def getallsteps(Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                SPRING_URL + "onboarding/getallsteps",
                headers={"Token": Token}
            )
            return response.json()
        except Exception as e:
            return {"code": 500, "message": str(e)}

@router.get("/getdevelopers")
async def getdevelopers(Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                SPRING_URL + "onboarding/getdevelopers",
                headers={"Token": Token}
            )
            return response.json()
        except Exception as e:
            return {"code": 500, "message": str(e)}

@router.delete("/deletestep/{id}")
async def deletestep(id: int, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.delete(
                SPRING_URL + f"onboarding/deletestep/{id}",
                headers={"Token": Token}
            )
            return response.json()
        except Exception as e:
            return {"code": 500, "message": str(e)}

@router.get("/getmyprogress/{email}")
async def getmyprogress(email: str, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                SPRING_URL + f"onboarding/getmyprogress/{email}",
                headers={"Token": Token}
            )
            return response.json()
        except Exception as e:
            return {"code": 500, "message": str(e)}

@router.put("/updatestatus/{progressId}/{status}")
async def updatestatus(progressId: int, status: str, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.put(
                SPRING_URL + f"onboarding/updatestatus/{progressId}/{status}",
                headers={"Token": Token}
            )
            return response.json()
        except Exception as e:
            return {"code": 500, "message": str(e)}

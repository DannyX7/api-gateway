from fastapi import APIRouter, Header
from typing import Dict
import httpx

router = APIRouter(prefix="/learning")

SPRING_URL = "http://localhost:8001/"

@router.get("/getstudents")
async def get_students(Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                SPRING_URL + "learning/getstudents",
                headers={"Token": Token}
            )
            return response.json()
        except Exception as e:
            return {"code": 500, "message": str(e)}

@router.get("/getallcourses")
async def get_all_courses(Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                SPRING_URL + "learning/getallcourses",
                headers={"Token": Token}
            )
            return response.json()
        except Exception as e:
            return {"code": 500, "message": str(e)}

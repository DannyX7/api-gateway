from fastapi import APIRouter, Header
from typing import Dict
import httpx

router = APIRouter()

NODE_URL = "https://taskservices-no9j.onrender.com"

@router.post("/help/seed")
async def seed_help():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(NODE_URL + "/help/seed")
            return response.json()
        except Exception as e:
            return {"code": 500, "message": f"Gateway Node error: {str(e)}"}

@router.post("/help/query")
async def query_help(data: Dict):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(NODE_URL + "/help/query", json=data)
            return response.json()
        except Exception as e:
            return {"code": 500, "message": f"Gateway Node error: {str(e)}"}

@router.post("/logs/add")
async def add_log(data: Dict):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(NODE_URL + "/logs/add", json=data)
            return response.json()
        except Exception as e:
            return {"code": 500, "message": f"Gateway Node error: {str(e)}"}

@router.get("/logs/all")
async def get_logs():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(NODE_URL + "/logs/all")
            return response.json()
        except Exception as e:
            return {"code": 500, "message": f"Gateway Node error: {str(e)}"}

@router.get("/history/all")
async def get_history():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(NODE_URL + "/history/all")
            return response.json()
        except Exception as e:
            return {"code": 500, "message": f"Gateway Node error: {str(e)}"}

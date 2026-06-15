from fastapi import APIRouter, Header
from models.schemas import SigninSchema, SignupSchema, UsersSchema
import httpx

router = APIRouter(prefix="/authservice")

SPRING_URL = "http://localhost:8001/"

@router.post("/signup")
async def signup(U: SignupSchema):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                SPRING_URL + "user/signup",
                json=U.model_dump()
            )
            return response.json()
        except Exception as e:
            return {"code": 500, "message": f"Gateway connection error: {str(e)}"}

@router.post("/signin")
async def signin(U: SigninSchema):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                SPRING_URL + "user/signin",
                json=U.model_dump()
            )
            return response.json()
        except Exception as e:
            return {"code": 500, "message": f"Gateway connection error: {str(e)}"}

@router.get("/uinfo")
async def uinfo(Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                SPRING_URL + "user/uinfo",
                headers={"Token": Token}
            )
            return response.json()
        except Exception as e:
            return {"code": 500, "message": str(e)}

@router.get("/profile")
async def profile(Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                SPRING_URL + "user/profile",
                headers={"Token": Token}
            )
            return response.json()
        except Exception as e:
            return {"code": 500, "message": str(e)}

@router.get("/getallusers/{PAGE}/{SIZE}")
async def getallusers(PAGE: int, SIZE: int, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{SPRING_URL}user/getallusers/{PAGE}/{SIZE}",
                headers={"Token": Token}
            )
            return response.json()
        except Exception as e:
            return {"code": 500, "message": str(e)}

@router.get("/getuser/{ID}")
async def getuser(ID: int, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{SPRING_URL}user/getuser/{ID}",
                headers={"Token": Token}
            )
            return response.json()
        except Exception as e:
            return {"code": 500, "message": str(e)}

@router.post("/saveuser")
async def saveuser(U: UsersSchema, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                SPRING_URL + "user/saveuser",
                json=U.model_dump(),
                headers={"Token": Token}
            )
            return response.json()
        except Exception as e:
            return {"code": 500, "message": str(e)}

@router.put("/updateuser/{ID}")
async def updateuser(ID: int, U: UsersSchema, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.put(
                SPRING_URL + f"user/updateuser/{ID}",
                json=U.model_dump(),
                headers={"Token": Token}
            )
            return response.json()
        except Exception as e:
            return {"code": 500, "message": str(e)}

@router.delete("/deleteuser/{ID}")
async def deleteuser(ID: int, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.delete(
                SPRING_URL + f"user/deleteuser/{ID}",
                headers={"Token": Token}
            )
            return response.json()
        except Exception as e:
            return {"code": 500, "message": str(e)}

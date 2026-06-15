from pydantic import BaseModel, EmailStr
from typing import Optional

class SigninSchema(BaseModel):
    username: str
    password: str

class SignupSchema(BaseModel):
    fullname: str
    phone: str
    email: EmailStr
    password: str
    retypepassword: str

class UsersSchema(BaseModel):
    id: Optional[str] = ""
    fullname: str
    phone: str
    email: EmailStr
    password: str
    role: int
    status: int

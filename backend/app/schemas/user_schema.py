from pydantic import BaseModel, EmailStr
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role:str = "customer"
    
class UserResponse(BaseModel):
    id :str
    name:str
    email:EmailStr
    role:str
    
    
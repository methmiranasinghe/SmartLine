from fastapi import APIRouter, HTTPException

from bson import ObjectId
from backend.app.databases import users_collection
from app.schemas.user_schema import UserCreate
from app.schemas.auth_schema import LoginRequest
from app.utils.auth import hashpassword, verify_password, create_access_token

router = APIRouter(prefix="/auth",tags=["auth"])
@router.post("/register")
def register_user(user: UserCreate):
    existing_user = users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered") 
    new_user = {
        "name":user.name,
        "email": user.email,
        "password": hashpassword(user.password),
        "role":user.role
    }
    result = users_collection.insert_one(new_user)
    return {"message": "User registered successfully",
            "user_id": str(result.inserted_id)
        }
@router.post("/login")
def login_user(login_data: LoginRequest):
    user = users_collection.find_one({"email":login_data.email})
    if not user:
        raise HTTPException(
            status_code = 401,
            detail="Invalid Email or password"
    )
    if not verify_password(login_data.password,user["password"]):
        raise HTTPException(
            status_code=401,
            detail="Invalid Email or password"
    )
    token=create_access_token({
        "user_id":str(user["_id"]),
        "email":user["email"],
        "role":user["role"]
    })
    
    return{
        "access_token":token,
        "token_type":"bearer",
        "user":{
            "id":str(user["_id"]),
            "name":user["name"],
            "email":user["email"],
            "role":user["role"]
        }
    }
    
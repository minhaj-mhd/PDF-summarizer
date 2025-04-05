from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email : EmailStr
    password: str

class UserOut(BaseModel):
    id : int
    email: EmailStr

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type : str
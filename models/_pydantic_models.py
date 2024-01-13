from pydantic import BaseModel

class TodoModelPydantic(BaseModel):
    title: str
    description: str

class UserModelPydantic(BaseModel):
    username: str
    password: str
    email: str

class FormLoginSchema(BaseModel):
    email   : str
    password: str

class SignupResponseModel(BaseModel):
    user_id: str

class LoginResponseModel(BaseModel):
    access_token : str
    token_type: str = "bearer"
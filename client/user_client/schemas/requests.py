from typing import List

from pydantic import BaseModel, Field, RootModel

class BaseUserRequestSchema(BaseModel):
    id: int = Field(alias="user_id")
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int = Field(alias="user_status")



class UserCreateRequestSchema(BaseUserRequestSchema):
    create_user: BaseUserRequestSchema

class UsersCreateRequestSchema(RootModel):
    create_users: List[UserCreateRequestSchema]

class UserUpdateRequestSchema(BaseUserRequestSchema):
    update_user: BaseUserRequestSchema





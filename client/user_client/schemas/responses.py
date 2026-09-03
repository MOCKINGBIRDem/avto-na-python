from pydantic import BaseModel, Field

class GetUserResponseSchema(BaseModel):
    id: int = Field(alias="user_id")
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int = Field(alias="user_status")

class BaseUserResponseSchema(BaseModel):
    code: int
    type: str
    message: str

class UserCreateResponseSchema(BaseUserResponseSchema):
    create_user_response: BaseUserResponseSchema

class UsersCreateResponseSchema(BaseUserResponseSchema):
    create_users_response: BaseUserResponseSchema

class UserUpdateResponseSchema(BaseUserResponseSchema):
    update_user_response: BaseUserResponseSchema

class UserLogoutResponseSchema(BaseUserResponseSchema):
    logout_user_response: BaseUserResponseSchema

class DeleteUserResponseSchema(BaseUserResponseSchema):
    delete_user_response: BaseUserResponseSchema



from _pydatetime import datetime

from pydantic import BaseModel, Field, RootModel, ConfigDict


class BaseUserRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_id: int = Field(alias="id")
    username: str
    first_name: str = Field(alias="firstName")
    last_name: str =  Field(alias="lastName")
    email: str
    password: str
    phone: str
    user_status: int = Field(alias="userStatus")



class UserCreateRequestSchema(BaseUserRequestSchema):
    pass

class UsersCreateRequestSchema(RootModel[list[UserCreateRequestSchema]]):
    pass

class UserUpdateRequestSchema(BaseUserRequestSchema):
    pass


class LoginUserQueryParams(BaseModel):
    username: str = Field(min_length=8)
    password: str = Field(min_length=12)


class PlaceAnOrderForAPet(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    order_id: int = Field(alias="id")
    pet_id: int = Field(alias="petId")
    quantity: int
    ship_date: datetime = Field(alias="shipDate")
    status: str
    complete: bool






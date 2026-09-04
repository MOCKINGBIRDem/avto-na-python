from _pydatetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class GetUserResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_id: int = Field(alias="id")
    username: str
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: str
    password: str
    phone: str
    user_status: int = Field(alias="userStatus")

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

class GetInventoryResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    available: int
    pending: int
    sold: int

class BaseStoreResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    order_id: int = Field(alias="id")
    pet_id: int = Field(alias="petId")
    quantity: int
    ship_date: datetime = Field(alias="shipDate")
    status: str
    complete: bool

class ReturnPetResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    additional_prop1: int = Field(alias="additionalProp1")
    additional_prop2: int = Field(alias="additionalProp2")
    additional_prop3: int = Field(alias="additionalProp3")

class FindOrderResponseSchema(BaseStoreResponseSchema):
    pass

class DeleteOrderResponseSchema(BaseStoreResponseSchema):
    code: int
    type: str
    message: str





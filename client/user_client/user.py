from http.client import responses

from httpx import Response, QueryParams, request

from base_api_method import BaseApiMethod
from client.user_client.schemas.requests import BaseUserRequestSchema, UserUpdateRequestSchema, \
    UsersCreateRequestSchema, UserCreateRequestSchema
from client.user_client.schemas.responses import BaseUserResponseSchema, GetUserResponseSchema, \
    UserUpdateResponseSchema, \
    DeleteUserResponseSchema, UserCreateResponseSchema, UsersCreateResponseSchema, UserLogoutResponseSchema


class UserClient(BaseApiMethod):

    def create_user_endpoint(
            self,
            request: UserCreateRequestSchema
    ) -> Response:

        return self.post(
            endpoint="/v2/user",
            json=request.model_dump(mode="json", by_alias=True, exclude_none=True)
        )

    def create_group_users_endpoint(
            self,
            request: UsersCreateRequestSchema
    ) -> Response:

        return self.post(
            endpoint="/v2/user/createWithList",
            json=request.model_dump(mode="json", by_alias=True, exclude_none=True)
        )

    def get_user_by_username_endpoint(
            self,
            username: str,
    ) -> Response:
        return self.get(
            endpoint=f"/v2/user/{username}",
        )

    def update_user_endpoint(
            self,
            request: UserUpdateRequestSchema,
            username: str,
    ) -> Response:
        return self.put(
            endpoint=f"/v2/user/{username}",
            json=request.model_dump(
                mode="json",
                by_alias=True,
                exclude_none=True
            )
        )

    def logout_user_endpoint(
            self,
    ) -> Response:
        return self.get(
            endpoint="/v2/user/logout",
        )

    def delete_user_endpoint(
            self,
            username: str,
    ) -> Response:
        return self.delete(
            endpoint=f"/v2/user/{username}",
        )

    def delete_user(
            self,
            username: str,
    ) -> DeleteUserResponseSchema:

        response = self.delete_user_endpoint(username=username)
        response.raise_for_status()
        return DeleteUserResponseSchema.model_validate_json(response.text)

    def update_user(
            self,
            request: UserUpdateRequestSchema,
            username: str,

    ) ->UserUpdateResponseSchema:

        response = self.update_user_endpoint(request=request, username=username)
        response.raise_for_status()
        return UserUpdateResponseSchema.model_validate_json(response.text)


    def create_user(
            self,
            request: UserCreateRequestSchema,

    ) -> UserCreateResponseSchema:

        response = self.create_user_endpoint(request=request)
        response.raise_for_status()
        return UserCreateResponseSchema.model_validate_json(response.text)

    def create_group_users(
            self,
            request: UsersCreateRequestSchema,

    ) -> UsersCreateResponseSchema:

        response = self.create_group_users_endpoint(request=request)
        response.raise_for_status()
        return UsersCreateResponseSchema.model_validate_json(response.text)



    def get_user_by_username(
            self,
            username: str,
    ) -> GetUserResponseSchema:

        response = self.get_user_by_username_endpoint(username=username)
        response.raise_for_status()
        return GetUserResponseSchema.model_validate_json(response.text)

    def logout_user(
            self,
    ) -> UserLogoutResponseSchema:

        response = self.logout_user_endpoint()
        response.raise_for_status()
        return UserLogoutResponseSchema.model_validate_json(response.text)



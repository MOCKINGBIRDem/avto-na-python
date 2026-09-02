from typing import Any

import allure
from httpx import Client, QueryParams, Response

class BaseApiMethod:

    def __init__(self, client: Client) -> None:
        self.client = client

    def get(
            self,
            endpoint: str,
            params: QueryParams | dict[str, Any] | None = None,
            headers: dict[str, str] | None = None
    ) -> Response:
        with allure.step(f"Выполнение Get-запроса {endpoint}"):
            return self.client.get(
                url=endpoint,
                params=params,
                headers=headers,
            )

    def post(
            self,
            endpoint: str,
            params: QueryParams | dict[str, Any] | None = None,
            json: dict[str, Any] | None = None,
            data: dict[str, Any] | None = None,
            files: dict[str, Any] | None = None,
            headers: dict[str, str] | None = None,


    ) -> Response:
        with allure.step(f"Выполнение Post-запроса {endpoint}"):
            return self.client.post(
                url=endpoint,
                params=params,
                json=json,
                data=data,
                files=files,
                headers=headers,

            )

    def put(
            self,
            endpoint: str,
            params: QueryParams | dict[str, Any] | None = None,
            json: dict[str, Any] | None = None,
            data: dict[str, Any] | None = None,
            files: dict[str, Any] | None = None,
            headers: dict[str, str] |None = None,

    ) -> Response:
        with allure.step(f"Выполнение Put-запроса {endpoint}"):
            return self.client.put(
                url=endpoint,
                params=params,
                json=json,
                data=data,
                files=files,
                headers=headers,
            )

    def patch(
            self,
            endpoint: str,
            params: QueryParams | dict[str, Any] | None = None,
            json: dict[str, Any] | None = None,
            data: dict[str, Any] | None = None,
            files: dict[str, Any] | None = None,
            headers: dict[str, str] | None = None,

    ) -> Response:
        with allure.step(f"Выполнение Patch-запроса {endpoint}"):
            return self.client.patch(
                url=endpoint,
                params=params,
                json=json,
                data=data,
                files=files,
                headers=headers,

            )

    def delete(
            self,
            endpoint: str,
            params: QueryParams | dict[str, Any] | None = None,

    ) -> Response:
        with allure.step(f"Выполнение Delete-запроса {endpoint}"):
            return self.client.delete(
                url=endpoint,
                params=params,
            )



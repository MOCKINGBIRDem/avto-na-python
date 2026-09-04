from base_api_method import BaseApiMethod
from client.user_client.schemas.requests import PlaceAnOrderForAPet
from httpx import Response, QueryParams, request

from client.user_client.schemas.responses import BaseStoreResponseSchema, GetInventoryResponseSchema, \
    FindOrderResponseSchema, DeleteOrderResponseSchema


class Store(BaseApiMethod):
    def place_an_order_endpoint(
            self,
            request: PlaceAnOrderForAPet,
    ) -> Response:

        return self.post(
            endpoint="/v2/store/order",
            json=request.model_dump(mode="json", by_alias=True, exclude_none=True)
        )

    def get_inventory_endpoint(
            self,
    ) -> Response:

        return self.get(
            endpoint="/v2/store/inventory",
            headers={"api_key": "special-key"}
        )

    def get_order_by_id_endpoint(
            self,
            order_id: int
    ) -> Response:
        return self.get(
            endpoint=f"/v2/store/order/{order_id}"
        )

    def delete_order_endpoint(
            self,
            order_id: int
    ) -> Response:

        return self.delete(
            endpoint=f"/v2/store/order/{order_id}"
        )


    def place_an_order(
            self,
            request: PlaceAnOrderForAPet
    ) -> BaseStoreResponseSchema:

        response = self.place_an_order_endpoint(request=request)
        response.raise_for_status()
        return BaseStoreResponseSchema.model_validate_json(response.text)

    def get_inventory(
            self,
    ) -> GetInventoryResponseSchema:

        response = self.get_inventory_endpoint()
        response.raise_for_status()
        return GetInventoryResponseSchema.model_validate_json(response.text)

    def get_order_by_id(
            self,
            order_id: int
    ) -> FindOrderResponseSchema:

        response = self.get_order_by_id_endpoint(order_id=order_id)
        response.raise_for_status()
        return FindOrderResponseSchema.model_validate_json(response.text)

    def delete_order(
            self,
            order_id: int
    ) -> DeleteOrderResponseSchema:

        response = self.delete_order_endpoint(order_id=order_id)
        response.raise_for_status()
        return DeleteOrderResponseSchema.model_validate_json(response.text)


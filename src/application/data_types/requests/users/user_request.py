from pydantic import UUID4, BaseModel, Field

from src.application.data_types.responses.api.base_response import (
    BaseApiResponse,
)


class NewUserPayload(BaseModel):
    account_id: UUID4


class UserPayload(BaseModel):
    account_id: UUID4
    name: str
    email: str
    cpf: str


class NewUserResponse(BaseApiResponse):
    payload: NewUserPayload


class GetPaginatedUserResponse(BaseApiResponse):
    payload: list[UserPayload] = Field(default=list)


class GetUserResponse(BaseApiResponse):
    payload: UserPayload


class UpdateUserResponse(BaseApiResponse):
    pass


class DeleteUserResponse(BaseApiResponse):
    pass

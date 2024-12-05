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


class PaginatedUsersPayload(BaseModel):
    users: list[UserPayload] = Field(default=list)
    total: int
    limit: int
    offset: int


class NewUserResponse(BaseApiResponse):
    payload: NewUserPayload


class GetPaginatedUsersResponse(BaseApiResponse):
    payload: PaginatedUsersPayload


class GetUserResponse(BaseApiResponse):
    payload: UserPayload


class UpdateUserResponse(BaseApiResponse):
    pass


class DeleteUserResponse(BaseApiResponse):
    pass

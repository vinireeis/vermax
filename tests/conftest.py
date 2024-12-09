from datetime import datetime, timedelta, timezone

import jwt as jwt_lib
import pytest_asyncio

from src.application.data_types.dtos.jwt_dto import (
    AccessTokenDto,
    JwtDecodedDto,
)
from src.application.data_types.requests.auth.jwt_request import (
    UserTokenDataRequest,
)
from src.application.services.token.jwt_token_service import JwtTokenService
from src.externals.infrastructures.ioc_container_config.witch_doctor_container_config_infrastructure import (
    WitchDoctorContainerConfigInfrastructure,
)

WitchDoctorContainerConfigInfrastructure.build_ioc_container()


@pytest_asyncio.fixture
def stub_user_token_data_request() -> UserTokenDataRequest:
    return UserTokenDataRequest(
        account_id='123e4567-e89b-12d3-a456-426655440000',
        cpf='102030',
        email='john@hotmail.com',
        exp=datetime.now(tz=timezone.utc) + timedelta(days=30),
        user_id=1,
    )


@pytest_asyncio.fixture
def mock_secret_key(monkeypatch):
    monkeypatch.setattr(JwtTokenService, name='_key', value='other_secret_key')


@pytest_asyncio.fixture
async def stub_valid_token(stub_user_token_data_request) -> AccessTokenDto:
    access_token = await JwtTokenService().generate_token(
        user_token_data_request=stub_user_token_data_request
    )
    return access_token


@pytest_asyncio.fixture
async def stub_expired_token(stub_user_token_data_request) -> AccessTokenDto:
    stub_user_token_data_request.exp = datetime.now(
        tz=timezone.utc
    ) - timedelta(minutes=1)
    access_token = await JwtTokenService().generate_token(
        user_token_data_request=stub_user_token_data_request
    )
    return access_token


@pytest_asyncio.fixture
async def stub_invalid_token(stub_user_token_data_request) -> AccessTokenDto:
    access_token = await JwtTokenService().generate_token(
        user_token_data_request=stub_user_token_data_request
    )
    return access_token


@pytest_asyncio.fixture(scope='function')
async def stub_decoded_token_raw(stub_valid_token) -> JwtDecodedDto:
    jwt_decoded_raw = jwt_lib.decode(
        jwt=stub_valid_token.access_token,
        key=JwtTokenService._key,
        algorithms=JwtTokenService._algorithm,
    )
    return jwt_decoded_raw

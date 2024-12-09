from unittest.mock import patch
from uuid import UUID

import pytest

from src.application.data_types.dtos.jwt_dto import (
    AccessTokenDto,
    JwtDecodedDto,
)
from src.application.services.token.jwt_token_service import JwtTokenService
from src.domain.exceptions.application.exception import (
    InvalidTokenException,
    TokenExpiredException,
)


@pytest.mark.asyncio
async def test_when_generate_token_with_success_then_returns_bearer_token(
    stub_user_token_data_request,
):
    bearer_token = await JwtTokenService().generate_token(
        user_token_data_request=stub_user_token_data_request
    )

    assert isinstance(bearer_token, AccessTokenDto)
    assert isinstance(bearer_token.access_token, str)
    assert isinstance(bearer_token.token_type, str)


async def test_when_generate_token_with_success_then_returns_bearer_token_type(
    stub_user_token_data_request,
):
    bearer_token = await JwtTokenService().generate_token(
        user_token_data_request=stub_user_token_data_request
    )
    assert bearer_token.token_type == 'bearer'


async def test_when_generate_token_successfully_then_pass(
    stub_user_token_data_request,
):
    bearer_token = await JwtTokenService().generate_token(
        user_token_data_request=stub_user_token_data_request
    )
    result = await JwtTokenService.validate_token(
        jwt=bearer_token.access_token
    )

    assert result is None


@patch('src.application.services.token.jwt_token_service.jwt_lib.encode')
async def test_when_generate_token_successfully_then_call_encode_method(
    mock_jwt_encode, stub_user_token_data_request
):
    await JwtTokenService().generate_token(
        user_token_data_request=stub_user_token_data_request
    )

    mock_jwt_encode.assert_called_once_with(
        payload=stub_user_token_data_request.model_dump(),
        key='my_secret_key',
        algorithm='HS256',
    )


async def test_when_expired_token_then_catch_expired_signature_error(
    stub_expired_token,
):
    with pytest.raises(TokenExpiredException):
        await JwtTokenService.validate_token(
            jwt=stub_expired_token.access_token
        )


async def test_when_invalid_token_signature_then_catch_invalid_signature_error(
    stub_invalid_token, mock_secret_key
):
    with pytest.raises(InvalidTokenException):
        await JwtTokenService.validate_token(
            jwt=stub_invalid_token.access_token
        )


async def test_when_invalid_token_then_catch_unexpected_error(mock_secret_key):
    access_token = 'invalid_token'

    with pytest.raises(InvalidTokenException):
        await JwtTokenService.validate_token(jwt=access_token)


async def test_when_decode_token_successfully_then_return_expected_jwt_dto(
    stub_valid_token,
):
    decoded_token_dto = await JwtTokenService.decode_token(
        jwt=stub_valid_token.access_token
    )

    assert isinstance(decoded_token_dto, JwtDecodedDto)
    assert isinstance(decoded_token_dto.account_id, UUID)
    assert isinstance(decoded_token_dto.user_id, int)
    assert isinstance(decoded_token_dto.cpf, str)
    assert isinstance(decoded_token_dto.email, str)


async def test_when_decode_token_successfully_then_return_expected_jwt_dto_values(
    stub_valid_token,
):
    decoded_token_dto = await JwtTokenService.decode_token(
        jwt=stub_valid_token.access_token
    )

    assert decoded_token_dto.cpf == '102030'
    assert decoded_token_dto.email == 'john@hotmail.com'
    assert decoded_token_dto.account_id == UUID(
        '123e4567-e89b-12d3-a456-426655440000'
    )
    assert decoded_token_dto.user_id == 1


@patch('src.application.services.token.jwt_token_service.jwt_lib.decode')
async def test_when_decode_token_successfully_then_call_jwt_decode_with_expected_values(
    mock_jwt_decode, stub_valid_token, stub_decoded_token_raw
):
    mock_jwt_decode.return_value = stub_decoded_token_raw
    await JwtTokenService.decode_token(jwt=stub_valid_token.access_token)
    mock_jwt_decode.assert_called_once_with(
        jwt=stub_valid_token.access_token,
        key='my_secret_key',
        algorithms='HS256',
    )


@patch('src.application.services.token.jwt_token_service.jwt_lib.decode')
@patch(
    'src.application.services.token.jwt_token_service.JwtTokenService._jwt_presenter'
)
async def test_when_decode_token_successfully_then_call_jwt_presenter_with_expected_values(
    mock_jwt_presenter,
    mock_jwt_decode,
    stub_valid_token,
    stub_decoded_token_raw,
):
    mock_jwt_decode.return_value = stub_decoded_token_raw
    await JwtTokenService.decode_token(jwt=stub_valid_token.access_token)
    mock_jwt_presenter.from_token_decoded_raw_to_jwt_dto.assert_called_once_with(
        token_decoded_raw=stub_decoded_token_raw
    )

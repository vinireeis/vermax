import jwt as jwt_lib
from decouple import config
from loguru import logger
from witch_doctor import WitchDoctor

from src.application.data_types.dtos.jwt_dto import (
    AccessTokenDto,
    JwtDecodedDto,
)
from src.application.data_types.requests.auth.jwt_request import (
    UserTokenDataRequest,
)
from src.application.ports.presenters.auth.i_jwt_presenter import IJwtPresenter
from src.application.ports.services.token.i_token_service import ITokenService


class JwtTokenService(ITokenService):
    _key = config('JWT_SECRET_KEY')
    _algorithm = config('JWT_ALGORITHM')
    _jwt_presenter: IJwtPresenter

    @WitchDoctor.injection
    def __init__(self, jwt_presenter: IJwtPresenter):
        JwtTokenService._jwt_presenter = jwt_presenter

    @classmethod
    async def generate_token(
        cls, user_token_data_request: UserTokenDataRequest
    ) -> AccessTokenDto:
        access_token = jwt_lib.encode(
            payload=user_token_data_request.model_dump(),
            key=cls._key,
            algorithm=cls._algorithm,
        )

        access_token_payload = cls._jwt_presenter.create_output_access_token(
            access_token=access_token
        )

        return access_token_payload

    @classmethod
    async def validate_token(cls, jwt: str) -> bool:
        try:
            jwt_lib.decode(jwt=jwt, key=cls._key, algorithms=cls._algorithm)
        except Exception as ex:
            logger.info(ex)
            return False
        return True

    @classmethod
    async def decode_token(cls, jwt: str) -> JwtDecodedDto:
        token_decoded_raw = jwt_lib.decode(
            jwt=jwt, key=cls._key, algorithms=cls._algorithm
        )

        jwt_decoded_dto = cls._jwt_presenter.from_token_decoded_raw_to_jwt_dto(
            token_decoded_raw=token_decoded_raw
        )

        return jwt_decoded_dto

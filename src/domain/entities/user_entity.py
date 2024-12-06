from uuid import UUID, uuid4

from pwdlib import PasswordHash

from src.domain.exceptions.domain.exception import (
    FailToGeneratePasswordHash,
    InvalidPassword,
)


class UserEntity:
    pwd_hash_lib = PasswordHash.recommended()

    def __init__(  # noqa: PLR0917 PLR0913
        self,
        name: str,
        email: str,
        cpf: str,
        password: str = None,
        password_hash: str = None,
        user_id: int = None,
        account_id: UUID = None,
    ):
        self.__name = name
        self.__email = email
        self.__cpf = cpf
        self.__password = password
        self.__password_hash = password_hash
        self.__user_id = user_id
        self.__account_id = account_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def password(self) -> str:
        return self.__password

    @property
    def account_id(self) -> UUID:
        return self.__account_id or uuid4()

    @property
    def password_hash(self):
        try:
            pw_hash_generated = self.pwd_hash_lib.hash(self.password)
            return pw_hash_generated
        except Exception as ex:
            raise FailToGeneratePasswordHash(original_error=ex)

    def validate_password(self, password: str) -> bool:
        pw_is_valid = self.pwd_hash_lib.verify(password, self.password_hash)
        if not pw_is_valid:
            raise InvalidPassword()
        return pw_is_valid

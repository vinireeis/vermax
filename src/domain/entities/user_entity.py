from uuid import UUID, uuid4

from pwdlib import PasswordHash


class UserEntity:
    pwd_hash = PasswordHash.recommended()

    def __init__(
        self,
        name: str,
        email: str,
        cpf: str,
        password: str,
        account_id: UUID = uuid4(),
    ):
        self.__name = name
        self.__email = email
        self.__cpf = cpf
        self.__password = password
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
        return self.__account_id

    @property
    def password_hash(self):
        return self.pwd_hash.hash(self.password)

    def validate_password(self) -> bool:
        pw_is_valid = self.pwd_hash.verify(self.password, self.password_hash)
        if not pw_is_valid:
            raise ValueError('Invalid password')
        return pw_is_valid

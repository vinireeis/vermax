from re import sub

from pydantic import BaseModel, EmailStr, field_validator, model_validator

# noqa: PLR2004


class NewUserRequest(BaseModel):
    name: str
    email: EmailStr
    cpf: str
    password: str

    @model_validator(mode='before')
    def validate_email_and_name_length(cls, values):
        if 'name' in values and len(values['name']) > 100:
            raise ValueError('nam e must be less than 100 characters')
        if 'email' in values and len(values['email']) > 100:
            raise ValueError('email must be less than 100 characters')
        return values

    @field_validator('password')
    def validate_password_length(cls, value):
        if len(value) < 4:
            raise ValueError('password must be greater than 3 characters')
        if len(value) > 20:
            raise ValueError('password must be less than 20 characters')
        return value

    @field_validator('cpf')
    def _get_only_numbers(cls, value: str) -> str:
        clean_cpf = sub(pattern=r'\D', repl='', string=value)

        if not len(clean_cpf) == 11:
            raise ValueError('cpf must be 11 digits long')

        first_digit = cls._validate_first_digit(clean_cpf)
        second_digit = cls._validate_second_digit(clean_cpf)

        if not clean_cpf[9] == first_digit and clean_cpf[10] == second_digit:
            raise ValueError('invalid cpf')

        return clean_cpf

    @staticmethod
    def _validate_first_digit(cpf: str) -> str:
        calc_1_digit = 0
        for i in range(10, 1, -1):
            calc_1_digit += int(cpf[10 - i]) * i

        calc_1_digit = (calc_1_digit * 10) % 11

        if calc_1_digit == 10:
            calc_1_digit = 0

        return str(calc_1_digit)

    @staticmethod
    def _validate_second_digit(cpf: str) -> str:
        calc_2_digit = 0
        for i in range(11, 1, -1):
            calc_2_digit += int(cpf[11 - i]) * i

        calc_2_digit = (calc_2_digit * 10) % 11

        if calc_2_digit == 10:
            calc_2_digit = 0

        return str(calc_2_digit)

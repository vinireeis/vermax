from pydantic import BaseModel, EmailStr, field_validator, model_validator

from src.application.data_types.requests.validators.cpf_validator import (
    CpfValidatorMixin,
)


class NewUserRequest(CpfValidatorMixin, BaseModel):
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

from enum import StrEnum


class TransactionOperationEnum(StrEnum):
    TRANSFER = 'TRANSFER'
    WITHDRAW = 'WITHDRAW'
    DEPOSIT = 'DEPOSIT'

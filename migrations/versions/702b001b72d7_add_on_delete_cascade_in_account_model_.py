"""add on delete, cascade in account_model, change balance to decimal

Revision ID: 702b001b72d7
Revises: 2d0d95be2111
Create Date: 2024-12-07 00:45:13.340769

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '702b001b72d7'
down_revision: Union[str, None] = '2d0d95be2111'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('accounts', 'balance',
               existing_type=sa.INTEGER(),
               type_=sa.DECIMAL(precision=10, scale=2),
               existing_nullable=False)
    op.drop_constraint('users_account_id_fkey', 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'accounts', ['account_id'], ['account_id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key('users_account_id_fkey', 'users', 'accounts', ['account_id'], ['account_id'])
    op.alter_column('accounts', 'balance',
               existing_type=sa.DECIMAL(precision=10, scale=2),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###

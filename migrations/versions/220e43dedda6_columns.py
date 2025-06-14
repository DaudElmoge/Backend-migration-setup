"""columns

Revision ID: 220e43dedda6
Revises: 7d760ce6ee72
Create Date: 2025-05-26 10:50:16.607620

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '220e43dedda6'
down_revision: Union[str, None] = '7d760ce6ee72'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('name', sa.Text(), nullable=True))
    op.add_column('products', sa.Column('price', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'price')
    op.drop_column('products', 'name')
    # ### end Alembic commands ###

"""add content column to posts table

Revision ID: 57a2c9e799ca
Revises: f9bc6fe909c4
Create Date: 2024-10-05 19:37:26.632190

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '57a2c9e799ca'
down_revision: Union[str, None] = 'f9bc6fe909c4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
